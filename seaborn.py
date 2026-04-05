import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
data = sns.load_dataset("tips")

print("Sample Data:")
print(data.head())

# ---------------- BAR PLOT ---------------- #
plt.figure()
sns.barplot(x="day", y="total_bill", data=data)
plt.title("Bar Plot")
plt.show()

# ---------------- LINE PLOT ---------------- #
plt.figure()
sns.lineplot(x="size", y="total_bill", data=data)
plt.title("Line Plot")
plt.show()

# ---------------- SCATTER PLOT ---------------- #
plt.figure()
sns.scatterplot(x="total_bill", y="tip", data=data)
plt.title("Scatter Plot")
plt.show()

# ---------------- HISTOGRAM ---------------- #
plt.figure()
sns.histplot(data["total_bill"], kde=True)
plt.title("Histogram")
plt.show()

# ---------------- BOX PLOT ---------------- #
plt.figure()
sns.boxplot(x="day", y="total_bill", data=data)
plt.title("Box Plot")
plt.show()

# ---------------- HEATMAP ---------------- #
plt.figure()
corr = data.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.title("Heatmap (Correlation Matrix)")
plt.show()