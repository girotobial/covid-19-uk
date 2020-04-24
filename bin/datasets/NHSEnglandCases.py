# NHSEnglandCases.py

import pandas as pd
import requests
from io import StringIO


class NHSEnglandCases:
    def __init__(
        self,
        URL=(r'https://coronavirus.data.gov.uk'
        r'/downloads/csv/coronavirus-cases_latest.csv'),
        date_cols=['Specimen date']
    ):
        self.csv = self._download_csv(URL)
        self._date_cols = date_cols
        self.df = self._dataframe()

    def _download_csv(self, URL):
        # Download using URL
        csv = requests.get(URL, stream=True).content

        # Decode from string
        csv = csv.decode('utf-8')

        return csv
    
    def _dataframe(self):
        '''Returns downloaded csv as a pandas dataframe'''
        df = pd.read_csv(
            StringIO(self.csv),
            parse_dates=self._date_cols
        )

        return df
    
    def _filter_area_type(self, _type):
        df = self.df
        return df[df['Area type'] == _type]

    def national(self, nation=None):
        df = self._filter_area_type('Nation')

        if nation is not None:
            df = df[df['Area name'] == nation]

        return df

    def regional(self, region=None):
        df = self._filter_area_type('Region')

        if region is not None:
            df = df[df['Area name'] == region]
        
        return df
   
    def utla(self, authority=None):
        df = self._filter_area_type('Upper tier local authority')

        if authority is not None:
            df = df[df['Area name'] == authority]
        
        return df
