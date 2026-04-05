import pandas as pd

# Create sample dataset
data = {
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Product": ["A", "A", "B", "B", "A", "B", "A", "B"],
    "Sales": [100, 150, 200, 130, 120, 180, 220, 140]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# ---------------- DATA ANALYSIS ---------------- #

# 1. Cross Tabulation (Frequency Table)
cross_tab = pd.crosstab(df["Region"], df["Product"])

print("\nCross Tabulation (Region vs Product):")
print(cross_tab)

# 2. Pivot Table (Summarized Insights)
pivot_table = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum"
)

print("\nPivot Table (Total Sales by Region & Product):")
print(pivot_table)

# 3. Additional Analysis
# Average sales by region
avg_sales = df.groupby("Region")["Sales"].mean()

print("\nAverage Sales by Region:")
print(avg_sales)

# Maximum sales by product
max_sales = df.groupby("Product")["Sales"].max()

print("\nMaximum Sales by Product:")
print(max_sales)