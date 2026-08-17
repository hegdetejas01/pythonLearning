import numpy as np

# Solving The system of linear equations
A = np.array([[1,3,4],[6,4,1],[2,2,2]])
B = np.array([5,16,11])
A_inverse = np.linalg.inv(A)
result = np.dot(A_inverse, B)
print(result)

A = np.array([[1,1],[4,3]])
B = np.array([5,15])
result = np.dot(np.linalg.inv(A), B)
print(result)