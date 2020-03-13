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


def calculate_derivative(iterable):
    change_list = []
    for i, val in enumerate(iterable):
        if i == 0:
            delta = 0

        if i > 0:
            delta = val - iterable[i - 1]

        change_list.append(delta)
    return change_list


def main():
    # Import data
    data_path = Path().cwd() / 'data'
    dataframe = pd.read_csv(data_path / 'DailyConfirmedCases.csv')

    dataframe['GrowthRatio'] = growth_ratio(dataframe['CumCases'])
    dataframe['SecondDerivativeCases'] = calculate_derivative(
        dataframe['CMODateCount']
    )
    dataframe.to_csv(
        data_path / 'DailyConfirmedCasesWithFeatures.csv',
        index=False
    )


if __name__ == '__main__':
    main()
