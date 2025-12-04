import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Dot product
print(np.dot(x, y))

#addition
print(x + y)     # [5 7 9]

#substraction
print(x - y)     # [-3 -3 -3]

#multiplication
print(x * y)     # [4 10 18]

#division
print(x / y)     # [0.25 0.4  0.5 ]

#exponent
print(x ** 2)

print("*********************")



#comparision and boolen operation
a = np.array([1, 2, 3, 4])

print(a > 2)           # [False False  True  True]
print(np.any(a > 2))   # True
print(np.all(a > 0))   # True

# Filter values
print(a[a > 2])        # [3 4]

print("*********************")





#Broadcasting
a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])

print(a + b)
# Output:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

print("*********************")






#Array maniplutation
a = np.array([[1, 2], [3, 4]])

print(np.transpose(a))     # [[1 3], [2 4]]
print(np.ravel(a))         # [1 2 3 4] (flatten)
print(a.flatten())         # Same as ravel but returns a copy
print(np.resize(a, (3, 2)))# Reshape to 3x2

print("*********************")





#stacking and splitting
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stacking
print(np.stack((a, b), axis=0))   # Vertical
print(np.stack((a, b), axis=1))   # Horizontal

# Splitting
c = np.array([1, 2, 3, 4, 5, 6])
print(np.split(c, 3))             # [[1 2], [3 4], [5 6]]

print("*********************")






#Aggregate functions
data = np.array([[1, 2, 3], [4, 5, 6]])

print(np.sum(data))              # 21
print(np.sum(data, axis=0))      # [5 7 9]
print(np.min(data))              # 1
print(np.max(data))              # 6
print(np.argmax(data))           # 5 (index of 6)

print("*********************")
