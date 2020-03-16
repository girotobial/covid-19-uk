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
        **kwargs
    )
    plt.yscale(yscale)
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
        title='Total Cases of COVID=19 over time in the UK',
        **kwargs
    )


def plot_new_cases(data, yscale='linear', **kwargs)
    _plot_cases(
        data,
        y='CMODateCount',
        yscale=yscale,
        ylabel='New Cases',
        title='New Confirmed Cases of COVID-19 in the UK',
        **kwargs
    )


def plot_growthfactor(data, **kwargs):
    data.plot(
        y='GrowthFactor',
        **kwargs
    )
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
    # TODO
    pass