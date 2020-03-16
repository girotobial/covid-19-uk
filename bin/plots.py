import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns 
from pathlib import Path
import bin.util as util


def plot_total_cases(data, yscale='linear', **kwargs):
    data.plot(
        y='CumCases',
        **kwargs
    )
    plt.yscale(yscale)
    _, top = plt.ylim()
    plt.ylim(0, top)
    plt.ylabel('Date')
    plt.ylabel('Cumulative Cases')
    plt.title('Cases of COVID-19 in the UK')
    plt.xticks(rotation=45, ha='right')
    plt.grid(which='major', axis='y')

    plt.tight_layout()
    sns.despine()

def plot_new_cases(data, yscale='linear', **kwargs)
    # TODO
    pass


def plot_growthfactor()
    # TODO
    pass

def main():
    # TODO
    pass