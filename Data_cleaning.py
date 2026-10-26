from ucimlrepo import fetch_ucirepo 
census_income = fetch_ucirepo(id=20)
df = census_income.data.original

original_shape = df.shape
original_duplicates = df.duplicated().sum()
original_missing = df.isnull().sum().sum()



print("first 5 rows:")
print(df.head())

print("\nShape of dataset:")
print(df.shape)

print("\ncoulmn names:")
print(df.columns)

print("\nMissing values in each column:")
print(df.isnull().sum())
print("\nData types each coulmn:")
print(df.dtypes)
print("\nUnique values in categorical columns:")
categorical_columns = df.select_dtypes(include="object").columns
for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].unique())
print("\nDuplicate rows:")
print(df.duplicated().sum())
print("\nSummary of numerical coulmns:")
print(df.describe())

import pandas as pd 
# Outlier detection using IQR method

numerical_columns = [
    'age',
    'fnlwgt',
    'education-num',
    'capital-gain',
    'capital-loss',
    'hours-per-week'
]

print("\nOutlier count using IQR method:")

for column in numerical_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    print(column, ":", len(outliers))
    # Handling outliers using IQR capping

for column in numerical_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df[column] = df[column].clip(
        lower=lower_bound,
        upper=upper_bound
    )

print("\nOutliers have been handled using IQR capping.")
# Removing duplicate rows
before_duplicates = len(df)

df = df.drop_duplicates()

after_duplicates = len(df)

print("\nDuplicate rows removed:", before_duplicates - after_duplicates)
print("Dataset shape after removing duplicates:", df.shape)

# Converting categorical columns into numerical form

categorical_columns = df.select_dtypes(include=['object']).columns

df = pd.get_dummies(
    df,
    columns=categorical_columns,
    drop_first=True
)

print("\nCategorical columns have been converted into numerical form.")
print("New shape of dataset:", df.shape)
print("\nBEFORE VS AFTER COMPARISON")

print("Original dataset shape: (48842, 15)")
print("Cleaned dataset shape:", df.shape)

print("Missing values after cleaning:", df.isnull().sum().sum())
print("Duplicate rows after cleaning:", df.duplicated().sum())
# Saving the cleaned dataset
df.to_csv("cleaned_census_income.csv", index=False)

print("Cleaned dataset has been saved successfully.")