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

# %%
sns.set(style='ticks', context='notebook')
plt.plot(
    data['CumCases'],
    data['CumDeaths']
)
plt.yscale('log')
plt.xscale('log')
plt.ylim(1, 10**5)
plt.xlim(1, 10**5)
plt.show()
