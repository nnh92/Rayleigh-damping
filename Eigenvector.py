import numpy as np

A = np.array([[3,0],
             [1,2]])

eig, v = np.linalg.eig(A)
print(eig)
print(v)