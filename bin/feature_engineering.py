import pandas as pd
from pathlib import Path
import numpy as np
from util import divide


def growth_ratio(iterable):
    growth_list = []
    for i, val in enumerate(iterable):
        if i == 0:
            ratio = 1

        if i > 0:
            ratio = divide(val, iterable[i - 1], 1)

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

    dataframe['GrowthFactor'] = growth_ratio(dataframe['CMODateCount'])
    dataframe['SecondDerivativeCases'] = calculate_derivative(
        dataframe['CMODateCount']
    )
    dataframe.to_csv(
        data_path / 'DailyConfirmedCasesWithFeatures.csv',
        index=False
    )


if __name__ == '__main__':
    main()
