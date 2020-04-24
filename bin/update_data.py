from arcgis.gis import GIS
from pathlib import Path
import pandas as pd
import requests
import io


def arcgis_download(public_data_id, data_path):
    # Setup gis
    gis = GIS()
    data_item = gis.content.get(public_data_id)
    
    # Download data
    data_item.download(save_path=data_path)

    # Import and convert to csv
    df = pd.read_excel(data_path / 'DailyConfirmedCases.xlsx')
    df.to_csv(data_path / 'DailyConfirmedCases.csv', index=False)

    # Delete xlsx file
    Path(data_path / 'DailyConfirmedCases.xlsx').unlink()


def download_nhs_england(
    URL=(r'https://coronavirus.data.gov.uk'
        r'/downloads/csv/coronavirus-cases_latest.csv')
):
    # Download csv from URL
    csv = requests.get(URL, stream=True).content

    # Parse csv with pandas and io
    df = pd.read_csv(
        io.StringIO(csv.decode('utf-8')),
        parse_dates=['Specimen date'],
    )

    return df


def main():
    # Setup gis
    public_data_id = 'e5fd11150d274bebaaf8fe2a7a2bda11'
    gis = GIS()
    data_item = gis.content.get(public_data_id)

    # Setup data directory
    data_path = Path('./data')

    if not data_path.exists():
        data_path.mkdir()

    # Download data
    data_item.download(save_path=data_path)

    # Import and convert to csv
    dataframe = pd.read_excel(data_path / 'DailyConfirmedCases.xlsx')
    dataframe.to_csv(data_path / 'DailyConfirmedCases.csv', index=False)

    # Delete xlsx file
    Path(data_path / 'DailyConfirmedCases.xlsx').unlink()


if __name__ == '__main__':
    main()
