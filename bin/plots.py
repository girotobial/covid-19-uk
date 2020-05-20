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


def plot_new_cases(data, y, ylabel, title, moving_average=False, **kwargs):
    # Esnure any existing plots are cleared
    plt.clf()

    # Make sure date values are in python date time
    data.reset_index(inplace=True)
    data['DateVal'] = pd.to_datetime(data['DateVal']).dt.to_pydatetime()

    # Plot bar chart
    plt.bar(data['DateVal'], data[y], **kwargs)
    if moving_average:
        plt.plot(data['DateVal'], data[y.rolling(7, center=True).mean()])
    plt.gca().xaxis_date()
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    today = date.today().strftime(r"%d/%m/%Y")
    plt.title(f'{title}({today})')
    plt.xticks(rotation=45, ha='right')
    plt.grid(which='major', axis='y')
    plt.tight_layout()
    sns.despine(left=True)


def plot_growthfactor(data, gf_column, ema_column, title, ma_label=None, **kwargs):
    plt.clf()
    data = data.reset_index()
    data['DateVal'] = pd.to_datetime(data['DateVal']).dt.to_pydatetime()
    
    plt.plot(
        data['DateVal'],
        data[gf_column],
        **kwargs,
        linestyle='--',
        alpha=0.5,
        label='Growth Factor'
    )
    alpha = 2 / (14 + 1)
    if ma_label is None:
        ma_label = f'Exponential Moving Average ($\\alpha$ ={alpha: .2f})'
    
    plt.plot(
        data['DateVal'],
        data[ema_column],
        **kwargs,
        label=ma_label,
        marker=None,
    )
    end_x = data[data[ema_column].notna()]['DateVal'].iloc[-1]
    end_y = data[data[ema_column].notna()][ema_column].iloc[-1]
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
    plt.title(f'{title} ({today})')
    left, right = plt.xlim()
    plt.hlines(1, left, right, ls='--', color='k')
    plt.xticks(rotation=45, ha='right')
    plt.grid(which='major', axis='y')
    plt.ylim(0, 2.5)
    plt.gcf().set_size_inches(*FIGSIZE)
    plt.tight_layout()
    sns.despine(left=True)


def plot_new_v_total_cases(data, cases_col, title, color, **kwargs):
    plt.clf()
    data['rolling_new_cases'] = data[cases_col].rolling(7).sum()
    data['cumulative'] = data[cases_col].expanding().sum()
    data = data[data[cases_col] > 10]

    plt.plot(
        data['cumulative'],
        data['rolling_new_cases'],
        color=color,
        **kwargs
    )
    end_x = data['cumulative'].iloc[-1]
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
    plt.title(f'{title} ({today})')
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
        y='CMODateCount',
        ylabel='New Cases',
        title='New Confirmed Cases (UK)',
        color='C1'
    )
    plt.savefig(path / 'new-cases.png')

    # Plot new cases growth factor
    plot_growthfactor(
        dailes,
        gf_column='GrowthFactor',
        ema_column='GF14DayEMA',
        title='COVID-19 New Cases Growth Factor (UK)',
        color='C2'
    )
    plt.savefig(path / 'growth-factor.png')

    # Plot test growth factor
    plot_growthfactor(
        dailes,
        gf_column='TestGrowthFactor',
        ema_column='TestGF14DayEMA',
        title='COVID-19 Tests Growth Factor (UK)',
        color='C5'
    )
    plt.savefig(path / 'tests-growth-factor.png')

    # Plot percent positive growth factor
    plot_growthfactor(
        dailes,
        gf_column='PositiveGrowthFactor',
        ema_column='PositiveGF14DayEMA',
        title='COVID-19 % Positive Tests Growth Factor (UK)',
        color='C7'
    )
    plt.savefig(path / 'positive-test-growth-factor.png')

    # Plot deaths growth factor
    plot_growthfactor(
        dailes,
        gf_column='GrowthFactorDeaths',
        ema_column='GFD14DayEMA',
        title='COVID-19 Deaths Growth Factor (UK)',
        color='C8'
    )
    plt.savefig(path / 'death-growth-factor.png')

    # Plot England growth factor by date of specimen
    plot_growthfactor(
        dailes.iloc[:-5, :],
        gf_column='GFSpecimenDate',
        ema_column='RollingGFSpecimenDate',
        title='COVID-19 Growth Factor by Specimen Date (England)',
        ma_label='7 Day Moving Average (Centered)',
        color='C2'
    )
    plt.savefig(path / 'specimen-date-growth-factor.png')

    # Plot trajectories
    plot_new_v_total_cases(
        dailes,
        'CMODateCount',
        'Trajectory of Covid-19 Confirmed Cases (UK)',
        color='C3',
        marker='.',
        markevery=[-1]
    )
    plt.savefig(path / 'trajectory.png')

    plot_new_v_total_cases(
        dailes.iloc[:-5, :].copy(),
        'EngConfSpecimens',
        'Trajectory of Covid-19 Confirmed Cases (England)',
        color='C3',
        marker='.',
        markevery=[-1]
    )
    plt.savefig(path / 'trajectory_england.png')

    plot_new_cases(
        dailes,
        y='EngConfSpecimens',
        ylabel='New Cases',
        title='New Confirmed Cases by Specimen Date (Eng)',
        color='C1'
    )
    plt.savefig(path / 'new-cases.png')

if __name__ == '__main__':
    main()