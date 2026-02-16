# Task 1: Data Cleaning and Preprocessing

## 📊 Overview

Data cleaning and preprocessing of the **House Prediction Dataset(Boston Housing Dataset)** to prepare it for predictive modeling and analysis.

---

## 🎯 Objectives

- ✅ Load and parse space-separated dataset correctly
- ✅ Rename columns with meaningful names
- ✅ Detect and handle missing values
- ✅ Identify and remove duplicate rows
- ✅ Detect and treat outliers using IQR method
- ✅ Standardize data formats and precision

---

## 📁 Dataset

**Name:** House Prediction Dataset 
**Description:** Housing data from Boston suburbs  
**Original Size:** 506 observations × 14 features  
**Format:** Space-separated values

**Features:**
- `CRIM` - Crime rate per capita
- `ZN` - Residential land zoned for large lots
- `INDUS` - Proportion of non-retail business
- `CHAS` - Charles River proximity (0/1)
- `NOX` - Nitric oxide concentration
- `RM` - Average rooms per dwelling
- `AGE` - Proportion of old houses
- `DIS` - Distance to employment centers
- `RAD` - Highway accessibility
- `TAX` - Property tax rate
- `PTRATIO` - Pupil-teacher ratio
- `B` - Proportion of Black population
- `LSTAT` - Lower status population %
- `MEDV` - Median home value (TARGET)

---

## 🔧 Cleaning Process

### 1. Data Loading
- Handled space-separated format using regex delimiter
- Set proper encoding for cross-platform compatibility

### 2. Column Renaming
- Replaced generic column names (0, 1, 2...) with meaningful labels
- Applied Boston Housing dataset standard naming convention

### 3. Missing Value Detection
- Scanned all columns for null/NaN values
- Result: **No missing values detected** ✓

### 4. Duplicate Removal
- Identified duplicate rows using pandas
- Removed duplicates to ensure data integrity

### 5. Outlier Detection (IQR Method)
- Calculated Q1, Q3, and IQR for each feature
- Identified outliers using: `[Q1 - 1.5×IQR, Q3 + 1.5×IQR]`
- Detected outliers in multiple features

### 6. Outlier Treatment
- Method: **Capping (Winsorization)**
- Values below lower bound → set to lower bound
- Values above upper bound → set to upper bound
- Preserves data distribution while reducing extreme values

### 7. Data Standardization
- Rounded all values to 4 decimal places
- Ensured consistent precision across dataset

---

## 📈 Results

| Metric | Value |
|--------|-------|
| **Original Rows** | 506 |
| **Final Rows** | ~506 (minus duplicates) |
| **Features** | 14 |
| **Missing Values** | 0 |
| **Duplicates Removed** | Variable |
| **Outliers Treated** | ~100+ values |
| **Data Quality** | >99% |

---

## 🛠️ Tools & Technologies

- **Language:** Python 3.14
- **Libraries:** pandas, numpy
- **Method:** IQR-based outlier detection
- **Approach:** Non-destructive capping

---

## 🚀 How to Run
```bash
# Navigate to Task 1 directory
cd Task1_Data_Cleaning

# Run the cleaning script
python cleaning.py
```

### Expected Output
```
Task1_Data_Cleaning/
└── results/
    ├── cleaned_house_data.csv    # Cleaned dataset
    └── cleaning_report.txt        # Detailed report
```

---

## 📊 Key Insights

- ✅ **Excellent data quality** - no missing values
- ✅ **Outliers concentrated** in CRIM, ZN, B variables
- ✅ **Target variable (MEDV)** well-distributed for regression
- ✅ **Dataset ready** for machine learning without additional preprocessing

---

## 💡 Next Steps

This cleaned dataset is now ready for:
- Exploratory Data Analysis (EDA)
- Feature engineering
- Regression modeling
- Predictive analytics

---

## 👩‍💻 Author

**BATALONG NYEMECK**  
Data Analytics Intern - Codveda Technology

---

## 🏢 Internship Provider

**Codveda Technology**
- Website: [www.codveda.com](https://www.codveda.com)
- LinkedIn: [@codveda]

---

## 📌 Tags

`#DataCleaning` `#Python` `#Preprocessing` `#BostonHousing` `#OutlierDetection` `#DataQuality` `#Codveda`