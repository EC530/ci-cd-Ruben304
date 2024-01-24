from MatrixMult import matrixMultiply
import numpy as np 

mOne = np.array([
[2, 4, 3, 1],
[2, 3, 6, 1]
])
mTwo = np.array([
[2, 1, 5, 2],
[4, 8, 3, 2]
])
mThree = np.array([
    [0,0,0,0],
    [0,0,0,0]
])

mFinal = matrixMultiply(mOne, mTwo)

print(mFinal)