import pandas as pd
from pathlib import Path
import numpy as np


def growth_ratio(iterable):
    growth_list = []
    for i, val in enumerate(iterable):
        if i == 0:
            ratio = 1

        if i > 0:
            ratio = val / iterable[i - 1]

        growth_list.append(ratio)
    return growth_list          


def main():
    # Import data
    data_path = Path().cwd() / 'data'
    dataframe = pd.read_csv(data_path / 'DailyConfirmedCases.csv')

    dataframe['GrowthRatio'] = growth_ratio(dataframe['CumCases'])


if __name__ == '__main__':
    main()
