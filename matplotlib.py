import matplotlib.pyplot as plt

# Sample Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# ---------------- LINE PLOT ---------------- #
plt.figure()
plt.plot(x, y)
plt.title("Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# ---------------- BAR CHART ---------------- #
categories = ["A", "B", "C", "D"]
values = [5, 7, 3, 8]

plt.figure()
plt.bar(categories, values)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# ---------------- PIE CHART ---------------- #
sizes = [30, 40, 20, 10]
labels = ["A", "B", "C", "D"]

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# ---------------- SCATTER PLOT ---------------- #
x_scatter = [1, 2, 3, 4, 5]
y_scatter = [5, 15, 10, 20, 25]

plt.figure()
plt.scatter(x_scatter, y_scatter)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()