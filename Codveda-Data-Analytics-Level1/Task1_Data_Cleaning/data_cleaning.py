import pandas as pd

#LOAD THE DATASET
df = pd.read_csv('Task1_Data_Cleaning\\data\\4) house Prediction Data Set.csv', sep=r'\s+', engine='python',header=None)
print(f"Dataset loaded successfully. First few rows:\n{df.head()}")
print(f"Dataset shape: {df.shape}")

#RENAMING COLUMNS
if df.shape[1] == 14:
    column_mapping = {
        0: 'CRIM', #Crime rate
        1: 'ZN', #Proportion of residential land zoned for lots over 25,000 sq.ft.
        2: 'INDUS', #Proportion of non-retail business acres per town
        3: 'CHAS', #Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
        4: 'NOX', #Nitric oxides concentration (parts per 10 million)
        5: 'RM',#Average number of rooms per dwelling
        6: 'AGE',#Proportion of owner-occupied units built prior to 1940
        7: 'DIS',#Weighted distances to five Boston employment centres
        8: 'RAD',#Index of accessibility to radial highways
        9: 'TAX',#Full-value property-tax rate per $10,000
        10: 'PTRATIO',#Pupil-teacher ratio by town
        11: 'B',#1000(Bk - 0.63)^2 where Bk is the proportion
        12: 'LSTAT',#Percentage of lower status of the population
        13: 'MEDV'#Median value of owner-occupied homes in $1000's
    }
    df.rename(columns=column_mapping, inplace=True)
    print(f"\nNew column names: {list(df.columns)}")
    print(f"\nNew dataset first few rows:\n{df.head()}")
    print(f"\nNew Dataset info:\n{df.info()}")

#MISSING VALUES
missing_values = df.isnull().sum()
print(f"\nMissing values in each column:\n{missing_values}")

#DUPLICATE VALUES
initial_rows=len(df)
duplicates = df.duplicated().sum()
if duplicates > 0:
    df=df.drop_duplicates(inplace=False)
    removed_duplicates = initial_rows - len(df)
    print(f"\n{removed_duplicates} duplicates removed. Number of rows after removal: {len(df)}")
else:
    print("\nNo duplicates found in the dataset.")

#OUTLIERS
outlier_summary = {}
for column in df.columns[:-1]:  # Exclude the target variable 'MEDV'
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    pourcentage_outliers = (len(outliers) / len(df)) * 100
    outlier_summary[column] = {
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'Lower Bound': lower_bound,
        'Upper Bound': upper_bound,
        'Outliers Count': len(outliers)
    }
    if len(outliers) > 0:
        print(f"\nColumn '{column}' : {len(outliers)} outliers detected ({pourcentage_outliers:.2f}%)")

#OUTLIERS TREATMENT
outlier_treated=0
for column in df.columns[:-1]:  
    Q1 = outlier_summary[column]['Q1']
    Q3 = outlier_summary[column]['Q3']
    IQR = outlier_summary[column]['IQR']
    lower_bound = outlier_summary[column]['Lower Bound']
    upper_bound = outlier_summary[column]['Upper Bound']
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    if len(outliers) > 0:
        df.loc[df[column] < lower_bound, column] = lower_bound
        df.loc[df[column] > upper_bound, column] = upper_bound
        outlier_treated += len(outliers)
        print(f"\nColumn '{column}' : {len(outliers)} outliers treated by replacing with bounds.")
print(f"\nTotal number of outliers treated: {outlier_treated}")

#DATA STANDARDISATION
print("\nRounding values to 4 decimal places.")
for column in df.columns[:-1]:  
    df[column]=df[column].round(4)
print("Values rounded to 4 decimal places") 

#FINAL DATASET
print(f"\nFinal dataset preview:\n{df.head()}")

#SAVE THE CLEANED DATASET
output_path = r'Task1_Data_Cleaning\results\cleaned_house_data.csv'
df.to_csv(output_path, index=False)
print(f"\nCleaned dataset successfully saved to: {output_path}")
