import numpy as np
import random
from itertools import permutations, combinations

vector1 = np.array([1, 2, 3])
print("Vector with scalar:")
print(vector1 + 1)  # [2 3 4]
print(vector1 - 2)  # [-1 0 1]
print(vector1 * 3)  # [3 6 9]

vector2 = np.array([2, 3, 1])
print("Vector with vector:")
print(vector1 + vector2)  # [3 5 4]
print(vector1 * vector2)  # Still element by element [2 6 3]
print(vector1 < vector2)  # [True True False]

boolVector1 = np.array([True, False, True, False])
boolVector2 = np.array([True, True, False, False])

print("Vector logic:")
print(np.logical_and(boolVector1, boolVector2))  # [True False False False]
print(np.logical_or(boolVector1, boolVector2))  # [True True True False]
print(np.logical_not(boolVector1))              # [False True False True]
print(np.logical_xor(boolVector1, boolVector2))  # [False True True False]

print("Dot product:")
print(np.dot(vector1, vector2))  # 11
print(vector1.dot(vector2))        # 11

# Matrices
matrix1 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
tempMatrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
matrix2 = np.asmatrix(tempMatrix2)
print(type(matrix1))  # <class 'np.matrix'>
print(type(tempMatrix2))  # <class 'np.ndarray'>
print(type(matrix2))  # <class 'np.matrix'>

print("Matrix with scalar:")
print(matrix1 + 1)  # [[2 3 4] [5 6 7] [8 9 10]]
print(matrix1 - 2)  # [[-1 0 1] [2 3 4] [5 6 7]]

# convert array to matrix using reshape
myArray = np.array([1, 2, 3, 4, 5, 6])
myMatrix = np.reshape(myArray, (2, 3))  # 2 rows, 3 columns
print(myMatrix)  # [[1 2 3] [4 5 6]]

# convert matrix to array using flatten
print(myMatrix.flatten())  # [1 2 3 4 5 6]

# transpose myMatrix
print(myMatrix.T)  # [[1 4] [2 5] [3 6]]

# let's see what happens when we try to invert a singular matrix
myDegenerateMatrix = np.matrix([[2, 2], [2, 2]])
try:
    print(np.linalg.inv(myDegenerateMatrix))
except np.linalg.LinAlgError:
    print(f"{myDegenerateMatrix} is singular and cannot be inverted")

# Matrix multiplication
print("Matrix dot product multiplication:")
# [[30 24 18] [84 69 54]] The number of rows in matrix2 must match the number of columns in myMatrix and is the number of rows in the final product matrix
print(np.dot(myMatrix, matrix2))
# [[30 24 18] [84 69 54]] * performs dot product becausse both are np.matrix objects np.array * performs element-wise multiplication
print(myMatrix * matrix2)

# Element by element multiplication
print("Element by element multiplication:")
print(np.multiply(matrix1, matrix2))  # [[9 16 21] [24 25 24] [21 16 9]]

# identity matrix
print("Identity matrix:")
print(np.identity(3))  # [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]]
print(np.eye(3))  # [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]]

# use the all close function to compare two matrices for equality
print("Comparing matrices:")
print(np.allclose(matrix1, matrix2))  # False

myRandomMatrix = np.random.random((3, 3))
print(myRandomMatrix)
myMatrixInverse = np.linalg.inv(myRandomMatrix)
print(np.allclose(myRandomMatrix.dot(myMatrixInverse), np.identity(3)))  # True

# Determinant
print("Determinant:")
print(np.linalg.det(matrix1))  # 0.0 because it is singular
print(np.linalg.det(matrix2))  # 0.0 because it is singular
print(np.linalg.det(myRandomMatrix))  # not 0.0 because it is not singular

# It is important to understand that a matrix cannot be inverted if it is singular.
# This is due to the fact that the determinant of a singular matrix is 0
# and the determinant is used as the denominator in the formula for the inverse of a matrix.

# Permutations
print("Permutations:")
myVector = np.array([1, 2, 3, 4])
print(np.random.permutation(myVector))  # [3 1 4 2]

for i in permutations(myVector):
    print(f"({i[0]}, {i[1]}, {i[2]}, {i[3]})")

# list comprehension
print("List comprehension:")
[print(f"({i[0]}, {i[1]}, {i[2]}, {i[3]})") for i in permutations(myVector)]

# Combinations
print("Combinations:")
for i in combinations(myVector, 2):
    print(f"({i[0]}, {i[1]})")

# list comprehension
print("List comprehension:")
[print(f"({i[0]}, {i[1]})") for i in combinations(myVector, 2)]

# sample
pool = []
comb = combinations(myVector, 2)
for i in comb:
    pool.append(i)

print(random.sample(pool, 2))


# Repetitions
listWithDuplicates = [1, 2, 2, 3, 3, 5, 6, 3, 4, 6, 7, 6, 5, 4, 4, 4]
deDuped = list(set(listWithDuplicates))
print(deDuped)  # [1, 2, 3, 4, 5, 6, 7]
