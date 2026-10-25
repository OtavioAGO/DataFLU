import pandas as pd
import matplotlib.pyplot as plt
publico = {"ANO" : ["2026", "2025", "2024", "2023", "2022", "2019", "2018", "2017", "2016"],
           "MEDIA_PUBLICO" : ["22,579", "26,724", "32,171", "29,783", "28,262", "20,209", "14,459", "14,432", "9,139"],
           "RANKING" : [11, 8, 5, 8, 7, 10, 11 ,9, 14]
           }
fluminense_df = pd.DataFrame(data=publico)
fluminense_df = fluminense_df.sort_values("ANO")
fig, ax = plt.subplots(figsize = (10, 6))

ax.plot(fluminense_df.ANO, fluminense_df.RANKING, marker='o', linestyle='-', color='#4C72B0', linewidth=2, markersize=8)

ax.set_ylim(20, 1)
ax.set_yticks(range(1, 21, 2))

for i, row in fluminense_df.iterrows():
    ax.text(str(row['ANO']), row['RANKING'] - 0.5, row.MEDIA_PUBLICO.replace(",", "."), 
            ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_xlabel('Ano')
ax.set_ylabel('Ranking')
ax.set_title('Ranking x Publico FFC')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()