import numpy as np
import logging

# Step 1: Create a function that that has two matrix inputs 
# and an output of the product of the given inputs
def matrixMult(matrixOne, matrixTwo):
    
    productMatrix = np.multiply(matrixOne, matrixTwo)
    logging.info('Matrix Multiplcation Completed')
    return productMatrix