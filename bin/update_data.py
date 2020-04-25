from pathlib import Path
import pandas as pd
from .datasets import NHSEnglandCases


def main():
    england = NHSEnglandCases().national()
    england = england[
        [
            'DateVal',
            'EngConfSpecimens',
            'CumEngConfSpec'
        ]
    ]
    conf_cases = pd.read_csv(
        Path('./data/DailyConfirmedCases.csv'),
        parse_dates=['DateVal']
    )
    conf_cases = conf_cases.merge(
        england,
        on='DateVal',
        how='left'
    )
    print(conf_cases)


if __name__ == '__main__':
    main()
