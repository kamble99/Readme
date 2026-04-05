import pandas as pd
import numpy as np

# Create sample DataFrame
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 25, None, 22, 25],
    "Marks": [85, 90, 88, None, 90],
    "City": ["Mumbai", "Pune", "Mumbai", "Delhi", "Pune"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# ---------------- DATA WRANGLING OPERATIONS ---------------- #

# 1. Handling Missing Values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

print("\nAfter Handling Missing Values:")
print(df)

# 2. Removing Duplicates
df.drop_duplicates(inplace=True)

print("\nAfter Removing Duplicates:")
print(df)

# 3. Renaming Columns
df.rename(columns={"Name": "Student_Name"}, inplace=True)

print("\nAfter Renaming Columns:")
print(df)

# 4. Changing Data Types
df["Age"] = df["Age"].astype(int)

print("\nAfter Changing Data Type:")
print(df.dtypes)

# 5. Filtering Data
filtered = df[df["Marks"] > 85]

print("\nFiltered Data (Marks > 85):")
print(filtered)

# 6. Sorting Data
sorted_df = df.sort_values(by="Marks", ascending=False)

print("\nSorted Data:")
print(sorted_df)

# 7. Creating New Column
df["Status"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("\nAfter Adding New Column:")
print(df)

# 8. Grouping Data
grouped = df.groupby("City")["Marks"].mean()

print("\nAverage Marks by City:")
print(grouped)

# 9. Reset Index
df.reset_index(drop=True, inplace=True)

print("\nFinal Cleaned Data:")
print(df)