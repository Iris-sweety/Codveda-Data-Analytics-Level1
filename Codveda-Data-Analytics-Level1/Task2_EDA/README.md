# Task 2: Exploratory Data Analysis (EDA)

## 📊 Overview

Comprehensive exploratory data analysis of the famous **Iris dataset**, identifying patterns, distributions, and relationships between features.


## 🎯 Objectives

- ✅ Calculate summary statistics (mean, median, mode, standard deviation)
- ✅ Visualize data distributions using histograms and boxplots
- ✅ Analyze correlations between numerical features
- ✅ Identify patterns and trends in the data


## 📁 Dataset

**Name:** Iris Dataset  
**Description:** Classic dataset containing measurements of iris flowers  
**Size:** 150 observations  
**Features:**
- `sepal_length` - Sepal length in cm
- `sepal_width` - Sepal width in cm
- `petal_length` - Petal length in cm
- `petal_width` - Petal width in cm
- `species` - Iris species (Setosa, Versicolor, Virginica)

**Source:** Provided by Codveda Technologies



## 🔍 Analysis Performed

### 1. Descriptive Statistics
- Mean, median, mode, standard deviation
- Variance, skewness, kurtosis
- Min, max, range for all numerical features

### 2. Data Quality Assessment
- Missing value detection
- Duplicate identification
- Data completeness verification

### 3. Correlation Analysis
- Pearson correlation matrix
- Identification of strong relationships between features

### 4. Distribution Analysis
- Histogram plots for each feature
- Box plots for outlier detection

### 5. Relationship Exploration
- Pairwise scatter plots by species
- Pattern identification across categories



## 📈 Key Findings

1. **Data Quality:** Excellent - no missing values, no duplicates
2. **Class Balance:** Perfectly balanced (50 samples per species)
3. **Strong Correlations:**
   - Petal length ↔ Petal width: 0.96
   - Sepal length ↔ Petal length: 0.87
   - Sepal length ↔ Petal width: 0.82
4. **Species Separation:** Setosa clearly distinguishable by petal measurements
5. **Outliers:** Minimal outliers detected across all features



## 🛠️ Tools & Technologies

| Category | Tools |
|----------|-------|
| **Language** | Python 3.14 |
| **Data Analysis** | pandas, numpy |
| **Visualization** | matplotlib, seaborn |
| **IDE** | VS Code |



## 📊 Visualizations

### Generated Plots:

1. **Distribution Histograms** (`distribution_histograms.png`)
   - Frequency distribution of each numerical feature

2. **Box Plots** (`box_plots.png`)
   - Outlier detection and quartile analysis

3. **Scatter Plots** (`scatter_plots.png`)
   - Pairwise relationships colored by species

4. **Correlation Heatmap** (`correlation_heatmap.png`)
   - Correlation coefficients between features



## 🚀 How to Run

### Prerequisites
- Python 3.8+
- Required packages (install via pip)

### Installation
```bash
# Navigate to Task 2 directory
cd Task2_EDA

# Install dependencies
pip install pandas numpy matplotlib seaborn

# Run the analysis
python eda_analysis.py
```

### Expected Output
```
Task2_EDA/
├── visualisations/
│   ├── distribution_histograms.png
│   ├── box_plots.png
│   ├── scatter_plots.png
│   └── correlation_heatmap.png
└── results/
    ├── eda_summary.csv
    ├── correlation_matrix.csv
    └── eda_report.txt
```


## 📋 Results Summary

| Metric | Value |
|--------|-------|
| **Total Observations** | 150 |
| **Features** | 5 (4 numeric, 1 categorical) |
| **Missing Values** | 0 |
| **Duplicates** | 0 |
| **Data Completeness** | 100% |
| **Classes** | 3 (perfectly balanced) |

---

## 💡 Insights for Machine Learning

- ✅ Dataset ready for classification without preprocessing
- ✅ Strong feature correlations suggest dimensionality reduction may help
- ✅ Clear separation between species indicates good classification potential
- ✅ No scaling required for tree-based models
- ✅ Recommended algorithms: Decision Trees, Random Forest, SVM, K-NN

---

## 📝 Project Structure
```
Task2_EDA/
├── README.md                       # This file
├── eda_analysis.py                # Main analysis script
├── data/
│   └── 1) iris.csv               # Dataset
├── visualisations/
│   ├── distribution_histograms.png
│   ├── box_plots.png
│   ├── scatter_plots.png
│   └── correlation_heatmap.png
└── results/
    ├── eda_summary.csv
    ├── correlation_matrix.csv
    └── eda_report.txt
```



## 👩‍💻 Author

**MADDIE BATALONG**  
Data Analytics Intern - Codveda Technologies



## 🏢 Internship Provider

**Codveda Technologies**
- Website: [www.codveda.com](https://www.codveda.com)
- LinkedIn: [@codveda]



## 📌 Tags

`#DataAnalytics` `#EDA` `#Python` `#DataVisualization` `#Iris` `#Statistics` `#MachineLearning` `#Codveda`
```


