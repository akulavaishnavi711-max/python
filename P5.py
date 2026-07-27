# Import pandas
import pandas as pd

# Load dataset
df = pd.read_csv("student_scores.csv")   # Replace with your file name 
print("First 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nDataset Shape (Rows, Columns):")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with column mean (numeric columns)
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Fill missing values in text columns with "Unknown"
text_cols = df.select_dtypes(include='object').columns
df[text_cols] = df[text_cols].fillna("Unknown")

print("\nMissing Values After Handling:")
print(df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicate Rows After Removal:", df.duplicated().sum())
print("\nStatistical Summary:")
print(df.describe)
df.to_csv("cleaned_student_scores.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_student_scores.csv'")