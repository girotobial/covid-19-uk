import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns 
from pathlib import Path
import bin.util as util


def _plot(
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
    sns.despine()


def plot_total_cases(data, yscale='linear', **kwargs):
    _plot(
        data,
        y='CumCases',
        yscale=yscale,
        ylabel='Total Cases',
        title='Total Cases of COVID=19 over time in the UK',
        **kwargs
    )


def plot_new_cases(data, yscale='linear', **kwargs)
    # TODO
    pass


def plot_growthfactor()
    # TODO
    pass

def main():
    # TODO
    pass