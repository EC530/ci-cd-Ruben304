import MatrixMult
import numpy as np
# create script similar to test_b.py
# mismatched matrix sizes

# function to check zero matrix input
def test_zeroMatrix():
    MatrixA = [[2, 4, 6], [9, 8, 7]]
    MatrixB = [[0, 0, 0], [0, 0, 0]]
    
    # changes matricies to array to make comparison easier
    ArrayMatrixA = np.array(MatrixA)
    ArrayMatrixB = np.array(MatrixB)

    # checks if either MatrixA or MatrixB is a zero matrix
    if np.all(ArrayMatrixA == 0) or np.all(ArrayMatrixB == 0):
        result = MatrixMult.matrixMultiply(MatrixA, MatrixB)
        # converts result to array for easier comparison
        result = np.array(result)
        # asserts result is a zero matrix
        assert np.all(result == 0)

# helper function to check character in matrix
def checkNumberMatrix(Matrix):
    for row in Matrix: # loop through all the rows in the Matrix
        for elements in row: # loop through all the elements in the row
            if not isinstance(elements, (int, float)): # checks if all the elements being looped are either a integer or float
                return False # if there is an element that is not int or float then it flags false
    return True # flags true if all the elements are int or float


def test_characterMatrix():
    MatrixA = [[2, 4, 6], ['b', 8, 7]]
    MatrixB = [[3, 0, 7], [6, 1, 8]]

    # if there is a character in the matrix then the test will fail/false
    # two nots are done because the only time it should flag True here is when the passed results are True and True
    if not checkNumberMatrix(MatrixA) or not checkNumberMatrix(MatrixB):
        assert False, "Characters found in matrix"
    else:
        assert True

# returns the number of columns in a given matrix
def sizeCheckMatrix(Matrix):
    matrixLen = 1000000
    tempLen = 0

    # it could look through every row and count the smallest number of columns meant to check of inhomogeneous shapes
    # but np.array (the method im utilizing to create the matrix already detect for this) ex: [[4,3],[2,2,2],[1]] will not be valid in numpy
    # so for right now it just gets the number of columns in the given matrix
    for row in Matrix:
        tempLen = len(row)
        if tempLen < matrixLen:
            matrixLen = tempLen
    return matrixLen


def test_validSizeMatrix():
    MatrixA = [[2, 4, 6], [9, 8, 7]]
    MatrixB = [[1, 3], [7, 9, 2]]

    # in numpy, the only requirement for matrix multiplcation is that both matricies have the same number of columns
    # and it will automcatically make inhomogenous matricies assert to false
    if sizeCheckMatrix(MatrixA) == sizeCheckMatrix(MatrixB):
        assert True
    else:
        assert False

