import pandas as pd

# Create first DataFrame
data1 = {
    "ID": [1, 2, 3, 4],
    "Name": ["A", "B", "C", "D"],
    "Age": [20, 25, 30, 22]
}

df1 = pd.DataFrame(data1)

# Create second DataFrame
data2 = {
    "ID": [1, 2, 3, 5],
    "Marks": [85, 90, 88, 75],
    "Grade": ["A", "A", "B", "C"]
}

df2 = pd.DataFrame(data2)

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

# Basic Operations
print("\nFirst 5 rows of df1:")
print(df1.head())

print("\nSummary Statistics of df2:")
print(df2.describe())

# Column Selection
print("\nSelect Name column from df1:")
print(df1["Name"])

# Row Selection
print("\nSelect first row of df1:")
print(df1.iloc[0])

# Add New Column
df1["City"] = ["Mumbai", "Pune", "Delhi", "Chennai"]
print("\nAfter Adding Column:")
print(df1)

# Filtering Data
filtered = df2[df2["Marks"] > 85]
print("\nFiltered Data (Marks > 85):")
print(filtered)

# Sorting
sorted_df = df2.sort_values(by="Marks", ascending=False)
print("\nSorted Data:")
print(sorted_df)

# ---------------- MERGE OPERATIONS ---------------- #

# Inner Merge (common IDs)
inner_merge = pd.merge(df1, df2, on="ID", how="inner")
print("\nInner Merge:")
print(inner_merge)

# Left Merge (all from df1)
left_merge = pd.merge(df1, df2, on="ID", how="left")
print("\nLeft Merge:")
print(left_merge)

# Right Merge (all from df2)
right_merge = pd.merge(df1, df2, on="ID", how="right")
print("\nRight Merge:")
print(right_merge)

# Outer Merge (all records)
outer_merge = pd.merge(df1, df2, on="ID", how="outer")
print("\nOuter Merge:")
print(outer_merge)

# GroupBy Operation
grouped = inner_merge.groupby("Grade")["Marks"].mean()
print("\nGroupBy (Average Marks by Grade):")
print(grouped)

# Save result
outer_merge.to_csv("merged_output.csv", index=False)

print("\nMerged data saved to merged_output.csv")