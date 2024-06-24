import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.colors import ListedColormap

df = pd.read_csv('finalcsv.csv')


df = df.drop(df.columns[[1,3,5,6, 8, 10, 11, 13, 15, 16, 18, 20]], axis = 1)
#df = df[df['Profession'] != 'scientist']
# removing % sign at the end
df.columns = [col.rstrip('%') for col in df.columns]
#df = df.sort_values(by='Profession')
df = df.sort_values(by='Profession', key=lambda col: col.str.lower())
print(df.head(50))
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
df.set_index('Profession', inplace=True)

print(df.head(50))

df_coloring = df.copy()
for colF, colM in zip(df_coloring.columns[::2], df_coloring.columns[1::2]):
    df_coloring[colF] = df[colF] > df[colM]
    df_coloring[colM] = df[colM] > df[colF]

sns.set_style('white')
plt.figure(figsize=(6.9, 8))
ax = sns.heatmap(df_coloring, cmap=ListedColormap(['#2c7bb6', '#d7191c']), annot=df, fmt=".0f", linewidths=.5, cbar=False)
countries = [l.get_text()[:-2] for l in ax.get_xticklabels()[::2]]
ax_top = ax.secondary_xaxis('top')
ax_top.set_xticks(ax.get_xticks(), [l.get_text()[-1:] for l in ax.get_xticklabels()])
ax_top.tick_params(length=0)
ax.set_xticks(range(1, len(df.columns), 2), countries)

for i in range(0, len(df.columns) + 1, 2):
    ax.axvline(i, lw=4, color='white')
for i in range(0, len(df) + 1):
    ax.axhline(i, lw=4, color='white')
ax.set_xlabel('Model and Gender')
ax.set_ylabel('Profession')
plt.tight_layout()
plt.savefig('research.png')