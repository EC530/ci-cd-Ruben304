from MatrixMult import matrixMultiply
import numpy as np 

mOne = np.array([
[2, 4, 3, 1],
[2, 3, 6, 1]
])
mTwo = np.array([
[2, 1], [2, 1]
])
# the numbers of columns must be the same for both matrix

def sizeCheckMatrix(Matrix):
    matrixLen = 1000000
    tempLen = 0

    for row in Matrix:
        tempLen = len(row)
        if tempLen < matrixLen:
            matrixLen = tempLen


    return matrixLen

mFinal = matrixMultiply(mOne, mTwo)
mLen = sizeCheckMatrix(mTwo)

print(mFinal)
print(mLen)

'''
Step 1:
Write an empty function that its input are two matrices (A and B) and its output is the multiplication of A and B (C = A.B)
Step 2:
Write test examples that will confirm your implementation based on the function defined in Step 1
This includes wrong inputs, error conditions and correct output
Step 3:
Write the details of the function
'''