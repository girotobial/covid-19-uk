import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
from pathlib import Path
import bin.util as util


def _plot_cases(
    data,
    y,
    yscale,
    ylabel,
    title,
    **kwargs
):
    data.plot(
        y=y,
        legend=None,
        **kwargs
    )
    plt.yscale(yscale)
    if yscale == 'linear':
        _, top = plt.ylim()
        plt.ylim(0, top)
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.grid(which='major', axis='y')
    plt.tight_layout()
    sns.despine(left=True)


def plot_total_cases(data, yscale='linear', **kwargs):
    _plot_cases(
        data,
        y='CumCases',
        yscale=yscale,
        ylabel='Total Cases',
        title='Total Cases of COVID-19 over time in the UK',
        **kwargs
    )


def plot_new_cases(data, **kwargs):
    # Esnure any existing plots are cleared
    plt.clf()

    # Make sure date values are in python date time
    data.reset_index(inplace=True)
    data['DateVal'] = pd.to_datetime(data['DateVal']).dt.to_pydatetime()

    # Plot bar chart
    plt.bar(data['DateVal'], data['CMODateCount'], **kwargs)
    plt.gca().xaxis_date()
    plt.xlabel('Date')
    plt.ylabel('New Cases')
    plt.title('New Cases per Day')
    plt.xticks(rotation=45, ha='right')
    plt.grid(which='major', axis='y')
    plt.tight_layout()
    sns.despine(left=True)


def plot_growthfactor(data, **kwargs):
    plt.clf()
    data.reset_index(inplace=True)
    data['DateVal'] = pd.to_datetime(data['DateVal']).dt.to_pydatetime()

    plt.plot(
        data['DateVal'],
        data['GrowthFactor'],
        **kwargs,
        linestyle='--',
        alpha=0.25,
        marker='.',
        label='Growth Factor'
    )
    plt.plot(
        data['DateVal'],
        data['GF5DayEMA'],
        **kwargs,
        label='GrowthFactor (5 Day EMA)',
        marker=None,
    )
    plt.plot(
        data['DateVal'],
        data['GF14DayEMA'],
        **kwargs,
        label='GrowthFactor (14 Day EMA)',
        marker=None,
        linestyle='dotted',
    )
    plt.gca().xaxis_date()
    plt.legend()
    plt.xlabel('Date'),
    plt.ylabel('Growth Factor'),
    plt.title('Growth Factor of COVID-19 by Date')
    left, right = plt.xlim()
    plt.hlines(1, left, right, ls='--', color='k')
    plt.xticks(rotation=45, ha='right')
    plt.grid(which='major', axis='y')
    plt.tight_layout()
    sns.despine(left=True)


def main():
    # Read in data
    path = Path().cwd()
    dailes = pd.read_csv(
        path / 'data' / 'DailyConfirmedCasesWithFeatures.csv',
        index_col='DateVal'
        )

    # Setup chart style
    sns.set(style='ticks', context='notebook')

    # Plot total cases with linear y axis
    plot_total_cases(
        dailes,
        marker='.',
        color='C0'
    )
    plt.savefig(path / 'confirmed-cases-linear-axis.png')

    # Plot total cases with logarithmic axis
    plot_total_cases(
        dailes,
        yscale='log',
        marker='.',
        color='C0'
    )
    plt.savefig(path / 'confirmed-cases-logarthimic-axis.png')

    # Plot new cases
    plot_new_cases(
        dailes,
        color='C1'
    )
    plt.savefig(path / 'new-cases.png')

    # Plot growth factor
    plot_growthfactor(
        dailes,
        color='C2'
    )
    plt.savefig(path / 'growth-factor.png')


if __name__ == '__main__':
    main()