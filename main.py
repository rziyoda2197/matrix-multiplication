import numpy as np

def matrix_multiply(A, B):
    return np.matmul(A, B)

# Misol uchun matritsalar
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(matrix_multiply(A, B))
```

```python
import numpy as np

def matrix_multiply(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("Matritsalar ko'paytmasi uchun matritsalar o'lchamlari mos bo'lishi kerak")
    
    result = np.zeros((A.shape[0], B.shape[1]))
    
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                result[i, j] += A[i, k] * B[k, j]
                
    return result

# Misol uchun matritsalar
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(matrix_multiply(A, B))
