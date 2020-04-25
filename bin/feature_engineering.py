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

    # Import and add test data
    tests = pd.read_csv(
        data_path / 'DailyTests.csv',
        parse_dates=['DateVal'],
        dayfirst=True
    )

    dataframe = dataframe.merge(
        tests,
        on='DateVal',
        how='left'
    )

    # Add growth factor and rolling averages
    dataframe['GrowthFactor'] = growth_ratio(dataframe['CMODateCount'])
    dataframe['GF5DayEMA'] = dataframe.GrowthFactor.ewm(
        span=5, adjust=False
        ).mean()
    dataframe['GF14DayEMA'] = dataframe.GrowthFactor.ewm(
        span=14, adjust=False
        ).mean()
    
    # Calculate Test Growth factor
    dataframe['TestGrowthFactor'] = growth_ratio(dataframe['TestCount'])
    dataframe['TestGF14DayEMA'] = dataframe.TestGrowthFactor.ewm(
        span=14, adjust=False
        ).mean()
    
    # Calculate postive test ratio and growth factor
    dataframe['PositiveRatio'] = np.round(
        dataframe['CMODateCount'] / dataframe['TestCount'],
        4
    )
    dataframe['PositiveGrowthFactor'] = growth_ratio(dataframe['PositiveRatio'])
    dataframe['PositiveGF14DayEMA'] = dataframe['PositiveGrowthFactor'].ewm(
        span=14, adjust=False
        ).mean()
    
    # Calculate growth factor for deaths

    dataframe['GrowthFactorDeaths'] = growth_ratio(dataframe['DailyDeaths'])
    dataframe['GFD14DayEMA'] = dataframe['GrowthFactorDeaths'].ewm(
        span=14,
        adjust=False
    ).mean()

    # Calculate growth derivative
    dataframe['GrowthDerivative'] = calculate_derivative(
        dataframe['CMODateCount']
    )

    # Calculate growth factor for cases by specimen date
    dataframe['GFSpecimenDate'] = growth_ratio(
        dataframe['EngConfSpecimens'].values
    )

    # Calculate rolling average GF by specimen date
    rolling_sum = dataframe['EngConfSpecimens'].rolling(7).sum()
    dataframe['RollingGFSpecimenDate'] = growth_ratio(rolling_sum.values)

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
