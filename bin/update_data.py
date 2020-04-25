from pathlib import Path
import pandas as pd
from .datasets import NHSEnglandCases


def main():
    data_path = Path('./data/DailyConfirmedCases.csv')
    england = NHSEnglandCases().national()
    england = england[
        [
            'DateVal',
            'EngConfSpecimens',
            'CumEngConfSpec'
        ]
    ]
    conf_cases = pd.read_csv(
        data_path,
        parse_dates=['DateVal']
    ).iloc[:, 0:5]
    conf_cases = conf_cases.merge(
        england,
        on='DateVal',
        how='left'
    )
    conf_cases.to_csv(data_path, index=False)


if __name__ == '__main__':
    main()
