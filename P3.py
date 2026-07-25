import numpy as np

# Create a 1D array
arr1 = np.array([10, 20, 30, 40, 50, 60])

# Create a 2D array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Display Arrays
print("1D Array:")
print(arr1)

print("\n2D Array:")
print(arr2)

# Array Properties
print("\n----- Array Properties -----")
print("Dimensions:", arr2.ndim)
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)

# Indexing
print("\n----- Indexing -----")
print("First element:", arr1[0])
print("Last element:", arr1[-1])
print("Element at row 2, column 3:", arr2[1, 2])
print("Element at row 3, column 1:", arr2[2, 0])

# Slicing
print("\n----- Slicing -----")
print("Elements from index 1 to 4:", arr1[1:5])
print("First 3 elements:", arr1[:3])
print("Elements from index 3 to end:", arr1[3:])
print("Every second element:", arr1[::2])
print("Reverse array:", arr1[::-1])

print("\nFirst row:", arr2[0, :])
print("Second column:", arr2[:, 1])
print("First two rows and last two columns:")
print(arr2[0:2, 1:3])

# Mathematical Operations
print("\n----- Mathematical Operations -----")
print("" \
"Addition:", arr1 + 5)
print("Multiplication:", arr1 * 2)

# Aggregate Functions
print("\n----- Aggregate Functions -----")
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))

# Reshape
print("\n----- Reshape -----")
new_arr = np.arange(1, 7).reshape(2, 3)
print(new_arr)