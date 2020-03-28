# %%
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
# %%
path = Path().cwd().parent
data = pd.read_csv(
    path / 'data' / 'DailyConfirmedCasesWithFeatures.csv',
    index_col='DateVal'
)

data.columns
# %%
data['rolling_new_cases'] = data['CMODateCount'].rolling(7).sum()
#data = data[data['CumCases'] > 10]
# %%
sns.set(style='ticks', context='notebook')
plt.plot(
    data['CumCases'],
    data['rolling_new_cases'],
)
plt.xscale('log')
plt.yscale('log')
plt.scatter(
    data['CumCases'][-1],
    data['rolling_new_cases'][-1],
    marker='o'
)
_, x_max = plt.xlim()
plt.xlim(10, x_max)
plt.ylim(10, x_max)
plt.ylabel('New Confirmed Cases (in the Past Week')
plt.xlabel('Total Confirmed Cases')
plt.title('Trajectory of Covid-19 Confirmed Cases (UK)')
plt.text(
    10,
    1,
    'Based on work by Aatish Bhatia & Minute Physics\nhttps://aatishb.com/covidtrends/ ')
plt.grid()
sns.despine()


# %%
