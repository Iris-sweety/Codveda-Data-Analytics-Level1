import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Task1_Data_Cleaning\\results\\cleaned_house_data.csv')
df['price_bin'] = pd.cut(df['MEDV'], bins=5,
                                labels=['<$15k', '$15-25k', '$25-35k', '$35-45k', '>$45k'])
# Bar Plot : nombre de maisons par tranche de prix
counts = df['price_bin'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(counts.index, counts.values,
              color=sns.color_palette('Blues_d', len(counts)), edgecolor='white')
ax.bar_label(bars, padding=3, fontsize=10)
ax.set_title('Boston Housing — Répartition par tranche de prix', fontsize=14, fontweight='bold')
ax.set_xlabel('Tranche de prix')
ax.set_ylabel('Nombre de maisons')
ax.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('Task3_Data_viz/housing_bar.png', dpi=150, bbox_inches='tight')
plt.show()

#Scatter Plot : RM vs MEDV coloré par LSTAT
fig, ax = plt.subplots(figsize=(7, 5))
sc = ax.scatter(df['RM'], df['MEDV'],
                c=df['LSTAT'], cmap='RdYlGn_r', alpha=0.7, edgecolors='white', s=60)
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label('% Population défavorisée (LSTAT)', fontsize=9)
ax.set_title('Boston Housing — Nbre de pièces vs Prix médian', fontsize=14, fontweight='bold')
ax.set_xlabel('Nombre moyen de pièces (RM)')
ax.set_ylabel('Prix médian ($000s)')
ax.grid(linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('Task3_Data_viz/housing_scatter.png', dpi=150, bbox_inches='tight')
plt.show()

#Line Chart : prix médian trié (tendance croissante)
fig, ax = plt.subplots(figsize=(10, 4))
sorted_medv = df['MEDV'].sort_values().reset_index(drop=True)
ax.plot(sorted_medv, color='#1976D2', linewidth=1.5, label='MEDV trié')
ax.fill_between(sorted_medv.index, sorted_medv, alpha=0.15, color='#1976D2')
ax.axhline(y=sorted_medv.mean(), color='red', linestyle='--', linewidth=1.2, label=f'Moyenne : {sorted_medv.mean():.1f}')
ax.set_title('Boston Housing — Tendance du prix médian', fontsize=14, fontweight='bold')
ax.set_xlabel('Rang (trié)')
ax.set_ylabel('Prix médian ($000s)')
ax.legend()
ax.grid(linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('Task3_Data_viz/housing_line.png', dpi=150, bbox_inches='tight')
plt.show()


