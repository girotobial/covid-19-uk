import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import ScalarFormatter
import pandas as pd
import seaborn as sns
from pathlib import Path
import bin.util as util
from datetime import date

FIGSIZE = (9.75, 6)

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

    # Change scientific yaxis to normal numbers
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    ax = plt.gca()
    ax.yaxis.set_major_formatter(formatter)
    plt.gcf().set_size_inches(*FIGSIZE)
    plt.tight_layout()
    sns.despine(left=True)


def plot_total_cases(data, yscale='linear', **kwargs):
    today = date.today().strftime(r"%d/%m/%Y")
    
    _plot_cases(
        data,
        y='CumCases',
        yscale=yscale,
        ylabel='Total Count',
        title=f'COVID-19 Confirmed Cases & Deaths in the UK ({today})',
        label='Confirmed Cases',
        **kwargs
    )
    plt.plot(
        data.index,
        data['CumDeaths'],
        label='Deaths',
        color='C1',
        marker='.'
    )
    plt.legend()


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
    today = date.today().strftime(r"%d/%m/%Y")
    plt.title(f'New Confimed Cases UK ({today})')
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
        alpha=0.5,
        label='Growth Factor'
    )
    alpha = 2 / (14 + 1)
    plt.plot(
        data['DateVal'],
        data['GF14DayEMA'],
        **kwargs,
        label=f'Exponential Moving Average ($\\alpha$ ={alpha: .2f})',
        marker=None,
    )
    end_x = data['DateVal'].iloc[-1]
    end_y = data['GF14DayEMA'].iloc[-1]
    plt.text(
        end_x,
        end_y,
        f'{end_y: .2f}',
        **kwargs,
        va='center',
    )
    plt.gca().xaxis_date()
    plt.legend()
    plt.xlabel('Date'),
    plt.ylabel('Growth Factor'),
    today = date.today().strftime(r"%d/%m/%Y")
    plt.title(f'COVID-19 Growth Factor in the UK ({today})')
    left, right = plt.xlim()
    plt.hlines(1, left, right, ls='--', color='k')
    plt.xticks(rotation=45, ha='right')
    plt.grid(which='major', axis='y')
    plt.ylim(0, 2)
    plt.gcf().set_size_inches(*FIGSIZE)
    plt.tight_layout()
    sns.despine(left=True)


def plot_new_v_total_cases(data, color, **kwargs):
    plt.clf()
    data['rolling_new_cases'] = data['CMODateCount'].rolling(7).sum()
    data = data[data['CumCases'] > 10]

    plt.plot(
        data['CumCases'],
        data['rolling_new_cases'],
        color=color,
        marker='.'
    )
    end_x = data['CumCases'].iloc[-1]
    end_y = data['rolling_new_cases'].iloc[-1]
    plt.text(
        end_x*1.2,
        end_y,
        f'Total:{end_x: .0f}\nNew:{end_y: .0f}',
        color=color,
        ha='left',
        va='center'
    )
    plt.xscale('log')
    plt.yscale('log')
    _, x_max = plt.xlim()
    plt.xlim(10, x_max * 5)
    plt.ylim(10, x_max)
    plt.ylabel('New Confirmed Cases (in the Past Week)')
    plt.xlabel('Total Confirmed Cases')
    today = date.today().strftime(r"%d/%m/%Y")
    plt.title(f'Trajectory of Covid-19 Confirmed Cases (UK) ({today})')
    plt.text(
        10,
        1,
        ('Based on work by Aatish Bhatia & Minute Physics'
        '\nhttps://aatishb.com/covidtrends/')
    )
    plt.grid(which='major')
    plt.gcf().set_size_inches(*FIGSIZE)
    sns.despine()


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

    plot_new_v_total_cases(
        dailes, 
        color='C3'
    )
    plt.savefig(path / 'trajectory.png')


if __name__ == '__main__':
    main()