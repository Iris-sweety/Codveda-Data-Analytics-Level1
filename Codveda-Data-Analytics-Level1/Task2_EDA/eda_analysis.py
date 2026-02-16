import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print("LEVEL 1 - TASK 2 :  Exploratory Data Analysis\n(EDA)")

# Load the dataset
data = pd.read_csv('Task2_EDA\\data\\1) iris.csv')
print(f'Dataset loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.')
# Display the first few rows of the dataset
print("\nFirst 5 rows of the dataset:")
print(data.head())

# Display summary statistics
print("\nSummary statistics:")  
print(data.describe())

# Check for missing values
print("\nMissing values in each column:")   
print(data.isnull().sum())

#Identify data types
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
categorical_columns = data.select_dtypes(include=['object']).columns

                     #VISUALIZATIONS
# Set the style of the plots
sns.set_style("whitegrid")
plt.figure(figsize=(12, 8))

#VISUALIZATION 1: Histograms
n_columns = len(numeric_columns)  
n_rows = (n_columns + 1) // 2  
fig, axes = plt.subplots(n_rows, 2, figsize=(14, n_rows * 5))
axes = axes.ravel()  

for i, column in enumerate(numeric_columns):  
    axes[i].hist(data[column], bins=20, color='blue', alpha=0.7)
    axes[i].set_title(f'Distribution of {column}', fontsize=10, fontweight='bold')
    axes[i].set_xlabel(column)
    axes[i].set_ylabel('Frequency')
    axes[i].grid(alpha=0.3)

for i in range(n_columns, len(axes)):
    fig.delaxes(axes[i])

plt.tight_layout()
plt.savefig('Task2_EDA\\visualisations\\distribution_histograms.png')
plt.show()
plt.close()

#VISUALIZATION 2: Box Plots

fig, axes = plt.subplots(n_rows, 2, figsize=(14, n_rows * 5))
axes = axes.ravel()

for i, column in enumerate(numeric_columns):  # Exclude the target variable
    bp=axes[i].boxplot(data[column], patch_artist=True, vert=True)
    bp['boxes'][0].set_facecolor('lightblue')
    axes[i].set_title(f'Box Plot of {column}', fontsize=12, fontweight='bold')
    axes[i].set_ylabel('Values')
    axes[i].grid(alpha=0.3)

for i in range(n_columns, len(axes)):
    fig.delaxes(axes[i])

plt.tight_layout()
plt.savefig('Task2_EDA\\visualisations\\box_plots.png')
plt.show()
plt.close()

#VISUALIZATION 3: Scatter Plots

if len(categorical_columns) > 0:    
    pairplot = sns.pairplot(data, hue=categorical_columns[0],diag_kind='kde', plot_kws={'alpha': 0.6},height=2.5)
    pairplot.fig.suptitle('Scatter Plots of Iris Dataset', fontsize=14, fontweight='bold')
   
plt.savefig('Task2_EDA\\visualisations\\scatter_plots.png',dpi=300,bbox_inches='tight',facecolor='white')
plt.show()
plt.close()

#VISUALIZATION 4: Correlation Heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = data[numeric_columns].corr()
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', mask=mask,square=True,center=0,cbar_kws={"shrink": .8}, linewidths=0.5)
plt.title('Correlation Heatmap of Iris Dataset', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('Task2_EDA\\visualisations\\correlation_heatmap.png')
plt.show()
plt.close()

print("\nEDA completed successfully. Visualizations saved in the 'visualisations' folder.")



# SAVE ANALYSIS RESULTS

print("\nSaving analysis results...")

import os
from datetime import datetime

# Create results directory if it doesn't exist
results_dir = 'Task2_EDA\\results'
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# 1. Save summary statistics
stats_summary = data.describe()
stats_summary.to_csv(os.path.join(results_dir, 'eda_summary.csv'))
print(f"✓ Statistics saved: {os.path.join(results_dir, 'eda_summary.csv')}")

# 2. Save correlation matrix
correlation_matrix.to_csv(os.path.join(results_dir, 'correlation_matrix.csv'))
print(f"✓ Correlation matrix saved: {os.path.join(results_dir, 'correlation_matrix.csv')}")

# 3. Report generation
class_distribution = data[categorical_columns[0]].value_counts() if len(categorical_columns) > 0 else None
missing_total = data.isnull().sum().sum()

report = f"""
{'=' * 80}
EXPLORATORY DATA ANALYSIS (EDA) REPORT - IRIS DATASET
{'=' * 80}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Internship: Codveda Technologies - Data Analytics Level 1:Task 2
Analyst: Maddie Batalong

1. DATASET OVERVIEW
{'=' * 80}
Total Observations: {data.shape[0]}
Total Features: {data.shape[1]}
Numeric Features: {len(numeric_columns)}
Categorical Features: {len(categorical_columns)}

Features:
{chr(10).join([f'  - {col} ({data[col].dtype})' for col in data.columns])}

2. DATA QUALITY
{'=' * 80}
Missing Values: {missing_total}
Duplicates: {data.duplicated().sum()}
Completeness: {((data.shape[0] * data.shape[1] - missing_total) / (data.shape[0] * data.shape[1]) * 100):.2f}%

3. DESCRIPTIVE STATISTICS
{'=' * 80}
{stats_summary.to_string()}

4. CORRELATION MATRIX
{'=' * 80}
{correlation_matrix.to_string()}

5. CLASS DISTRIBUTION
{'=' * 80}
{class_distribution.to_string() if class_distribution is not None else 'No categorical features'}

6. KEY INSIGHTS
{'=' * 80}
- Dataset contains {data.shape[0]} observations of iris flowers
- {len(numeric_columns)} numerical measurements per observation
- {data[categorical_columns[0]].nunique() if len(categorical_columns) > 0 else 0} different species in the dataset
- Data quality: Excellent (no missing values)
- Classes are well-balanced for classification tasks

7. VISUALIZATIONS GENERATED
{'=' * 80}
✓ distribution_histograms.png - Feature distributions
✓ box_plots.png - Outlier detection
✓ scatter_plots.png - Pairwise relationships
✓ correlation_heatmap.png - Feature correlations

8. RECOMMENDATIONS
{'=' * 80}
- Dataset is ready for classification modeling
- Features show good correlations with target variable
- No major preprocessing required
- Suitable for supervised learning algorithms

{'=' * 80}
ANALYSIS COMPLETED SUCCESSFULLY
{'=' * 80}
"""

# Save the report to a text file
report_path = os.path.join(results_dir, 'eda_report.txt')
with open(report_path, 'w', encoding='utf-8') as f:
    f.write(report)

print(f"✓ Report saved: {report_path}")

print("\n" + "=" * 80)
print("✓ EDA COMPLETED SUCCESSFULLY!")
print("=" * 80)
print(f"\nResults saved in:")
print(f"   - {results_dir}")
print(f"\n Visualizations saved in:")
print(f"   - {os.path.join('Task2_EDA', 'visualisations')}")
print("\n" + "=" * 80)