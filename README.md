Week 1 – Data Acquisition, Cleaning and Preprocessing

Project Overview

This project focuses on acquiring, cleaning, and preprocessing the Census Income dataset obtained from the UCI Machine Learning Repository. The main purpose of the project is to identify and handle data quality issues such as missing values, duplicate records, outliers, and categorical data.

Dataset

Dataset: Census Income
Source: UCI Machine Learning Repository
Dataset ID: 20

The dataset contains information related to demographic and employment characteristics and is used for income classification.

Tools and Technologies
	•	Python
	•	Pandas
	•	NumPy
	•	Matplotlib
	•	Seaborn
	•	VS Code

Data Cleaning Steps

The following steps were performed:
	1.	Loaded the dataset using Python.
	2.	Explored the dataset structure and column information.
	3.	Checked for missing values.
	4.	Checked for duplicate rows.
	5.	Identified outliers in numerical columns using the IQR method.
	6.	Handled outliers using IQR capping.
	7.	Removed duplicate rows.
	8.	Converted categorical variables into numerical form using one-hot encoding.
	9.	Verified the cleaned dataset.
	10.	Saved the final cleaned dataset as a CSV file.

Before and After Results
	•	Original dataset: 48,842 rows and 15 columns
	•	Duplicate rows removed: 58
	•	Final cleaned dataset: 48,784 rows and 103 columns
	•	Missing values after cleaning: 0
	•	Duplicate rows after cleaning: 0

The increase in the number of columns is due to one-hot encoding of categorical variables.

Files in This Project
Data_cleaning.py` — Python script for data cleaning and preprocessing.
cleaned_census_income.zip` — ZIP archive containing the cleaned dataset.
Week1_Data_cleaning_Report.docx` — Week 1 internship report.
README.md` — Project documentation.

Conclusion

The dataset was successfully cleaned and preprocessed using Python. Missing values, duplicate records, and outliers were addressed, and categorical variables were converted into numerical form. The resulting dataset is suitable for further data analysis and machine learning tasks.

