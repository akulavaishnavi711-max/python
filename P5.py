import pandas as pd

# Load the dataset
df = pd.read_csv("student_scores.csv")

# Display the first 5 rows
print("First 5 Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with the column mean (for numeric columns)
df.fillna(df.mean(numeric_only=True), inplace=True)

# OR remove rows with missing values
# df.dropna(inplace=True)

# Check for duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Display statistical summary
print("\nDataset Statistics:")
print(df.describe())

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Check missing values again
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df.head())