import numpy as np

## 1. Creating NumPy Arrays

# From a Python list
list_data = [1, 2, 3, 4, 5]
arr_from_list = np.array(list_data)
print("1. Array from list:", arr_from_list)
print("   Type:", type(arr_from_list))
print("   Shape:", arr_from_list.shape) # (5,) means 1-dimensional array with 5 elements
print("   Data type:", arr_from_list.dtype) # int32 or int64 depending on system

# From nested Python lists (2D array/matrix)
nested_list_data = [[1, 2, 3], [4, 5, 6]]
arr_2d = np.array(nested_list_data)
print("\n   2D Array from nested list:\n", arr_2d)
print("   Shape:", arr_2d.shape) # (2, 3) means 2 rows, 3 columns
print("   Number of dimensions (ndim):", arr_2d.ndim)

# Arrays with initial placeholders
arr_zeros = np.zeros((3, 4)) # 3x4 array filled with zeros
print("\n2. Array of zeros (3x4):\n", arr_zeros)

arr_ones = np.ones((2, 2)) # 2x2 array filled with ones
print("\n   Array of ones (2x2):\n", arr_ones)

arr_empty = np.empty((2, 3)) # 2x3 array with uninitialized (random) data
print("\n   Empty array (2x3 - values are random):\n", arr_empty)

arr_full = np.full((2, 2), 7) # 2x2 array filled with a specific value (7)
print("\n   Array filled with 7 (2x2):\n", arr_full)

# Arrays with a range of numbers
arr_range = np.arange(10) # 0 to 9
print("\n   Array with arange(10):", arr_range)

arr_range_step = np.arange(1, 10, 2) # Start, Stop (exclusive), Step
print("   Array with arange(1, 10, 2):", arr_range_step)

arr_linspace = np.linspace(0, 10, 5) # 5 evenly spaced numbers from 0 to 10 (inclusive)
print("   Array with linspace(0, 10, 5):", arr_linspace)

# Identity matrix (square matrix with ones on the main diagonal, zeros elsewhere)
identity_matrix = np.eye(3) # 3x3 identity matrix
print("\n   Identity Matrix (3x3):\n", identity_matrix)

## 2. Basic Array Operations

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Element-wise addition
print("\n3. Element-wise Addition:\n", arr1 + arr2)

# Element-wise multiplication
print("\n   Element-wise Multiplication:\n", arr1 * arr2)

# Matrix multiplication (dot product)
print("\n   Matrix Multiplication (Dot Product):\n", arr1 @ arr2) # or np.dot(arr1, arr2)

# Scalar operations
print("\n   Scalar Addition (arr1 + 10):\n", arr1 + 10)
print("\n   Scalar Multiplication (arr1 * 2):\n", arr1 * 2)

# Transposing a matrix
print("\n   Transposed arr1:\n", arr1.T)

## 3. Indexing and Slicing

my_arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# Accessing a single element
print("\n4. First element:", my_arr[0])
print("   Last element:", my_arr[-1])

# Slicing (start:end:step)
print("   Elements from index 2 to 5 (exclusive):", my_arr[2:6])
print("   Elements from the beginning to index 4 (exclusive):", my_arr[:5])
print("   Elements from index 3 to the end:", my_arr[3:])
print("   Every other element:", my_arr[::2])
print("   Reversed array:", my_arr[::-1])

# 2D array indexing
arr_2d_idx = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n   2D array for indexing:\n", arr_2d_idx)
print("   Element at row 1, col 2:", arr_2d_idx[1, 2]) # Accessing element (row, column)
print("   First row:", arr_2d_idx[0, :]) # All columns in first row
print("   Second column:", arr_2d_idx[:, 1]) # All rows in second column
print("   Sub-array (rows 0-1, cols 1-2):\n", arr_2d_idx[0:2, 1:3])