# NHSEnglandCases.py

import pandas as pd
import requests
from io import StringIO


class NHSEnglandCases:
    def __init__(self, URL, date_cols=['Specimen date']):
        self.csv = self._download_csv(URL)
        self._date_cols = date_cols

    def _download_csv(self, URL):
        csv = requests.get(URL, stream=True).content
        csv = csv.decode('utf-8')
        return csv
    
    @property
    def dataframe(self):
        df = pd.read_csv(
            StringIO(self.csv),
            parse_dates=self._date_cols
        )
        return df
