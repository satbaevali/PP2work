import numpy as np

# Given matrix A
A = np.array([[2, 5, 7], [6, 3, 4], [5, -2, -3]])

# Calculate the inverse of A
A_inverse = np.linalg.inv(A)

print("Inverse of A:")
print(A_inverse)
