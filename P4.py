

import pandas as pd

# Load the dataset
df = pd.read_csv("student_scores.csv")

# Display the first 5 rows
print("First 5 Rows:")
print(df.head())

# Display the last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Display the number of rows and columns
print("\nShape of Dataset:")
print(df.shape)

# Display the row count
print("\nNumber of Rows:")
print(df.shape[0])

# Display the column count
print("\nNumber of Columns:")
print(df.shape[1])

# Display the column names
print("\nColumn Names:")
print(df.columns)

# Display dataset information
print("\nDataset Information:")
print(df.info())
Example Output
If the dataset contains 25 rows and 2 columns (Hours and Scores), the output will look similar to:

Shape of Dataset:
(25, 2)

Number of Rows:
25

Number of Columns:
2

Column Names:
Index(['Hours', 'Scores'], dtype='object')

Dataset Information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 25 entries, 0 to 24
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Hours   25 non-null     float64
 1   Scores  25 non-null     int64
dtypes: float64(1), int64(1)
memory usage: ...
None
If you are using a different student score dataset (such as a CSV with Math, Reading, and Writing scores), upload the file or share its name, and I'll provide the exact code for that dataset.


