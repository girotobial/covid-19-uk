from arcgis.gis import GIS
from pathlib import Path


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

if __name__ == '__main__':
    main()
