import numpy as np

Matrix Operations
8️⃣ Matrix Addition

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

result = a + b
print(result)


# matrix maltiplixation
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

result = np.dot(a, b)
print(result)

# transpose of matrix
a = np.array([[1,2,3],[4,5,6]])

print(a.T)