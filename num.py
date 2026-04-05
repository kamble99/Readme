import numpy as np

# Create arrays
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print("Array a:", a)
print("Array b:", b)

# Arithmetic Operations
print("\nArithmetic Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Statistical Operations
print("\nStatistical Operations:")
print("Mean of a:", np.mean(a))
print("Sum of a:", np.sum(a))
print("Max of a:", np.max(a))
print("Min of a:", np.min(a))
print("Standard Deviation:", np.std(a))

# Reshaping Arrays
print("\nReshaping:")
c = np.array([[1, 2], [3, 4], [5, 6]])
print("Original:\n", c)

reshaped = c.reshape(2, 3)
print("Reshaped (2x3):\n", reshaped)

# Indexing and Slicing
print("\nIndexing & Slicing:")
print("First element:", a[0])
print("Last two elements:", a[2:])

# Matrix Operations
print("\nMatrix Operations:")
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print("Matrix Multiplication:\n", np.dot(m1, m2))
print("Transpose of m1:\n", m1.T)

# Random Numbers
print("\nRandom Numbers:")
rand_array = np.random.rand(3, 3)
print(rand_array)

# Boolean Operations
print("\nBoolean Operations:")
print(a > 2)
print(a[a > 2])