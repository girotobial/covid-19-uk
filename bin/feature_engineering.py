import pandas as pd
from pathlib import Path
import numpy as np
from bin.util import divide


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


def main(dataframe=None):
    data_path = Path().cwd() / 'data'

    if dataframe is None:
        # Import data
        dataframe = pd.read_csv(
            data_path / 'DailyConfirmedCases.csv',
            parse_dates=['DateVal'],
            dayfirst=True
        )


    # Add growth factor
    dataframe['GrowthFactor'] = growth_ratio(dataframe['CMODateCount'])

    # Calculate growth derivative
    dataframe['GrowthDerivative'] = calculate_derivative(
        dataframe['CMODateCount']
    )

    # Date features
    dataframe['Year'] = dataframe['DateVal'].dt.year
    dataframe['Month'] = dataframe['DateVal'].dt.month
    dataframe['Day'] = dataframe['DateVal'].dt.day
    dataframe['Week'] = dataframe['DateVal'].dt.week

    # Output to file
    dataframe.to_csv(
        data_path / 'DailyConfirmedCasesWithFeatures.csv',
        index=False
    )


if __name__ == '__main__':
    main()
