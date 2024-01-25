import numpy as np

# Step 1: Create a function that that has two matrix inputs 
# and an output of the product of the given inputs
def matrixMultiply(matrixOne, matrixTwo):
    
    # add if case of being zero
    if matrixOne == 0 or matrixTwo == 0:
        return 0 
    
    productMatrix = np.multiply(matrixOne, matrixTwo)
    return productMatrix