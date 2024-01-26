import numpy as np

# Step 1: Create a function that that has two matrix inputs 
# and an output of the product of the given inputs
def matrixMultiply(matrixOne, matrixTwo):
    
    productMatrix = np.multiply(matrixOne, matrixTwo)
    return productMatrix