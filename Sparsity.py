from numpy import array
from numpy import count_nonzero
import numpy as np


# create dense matrix
A = array([[1, 1, 0, 1, 0, 0], [1, 0, 2, 0, 0, 1], [99, 0, 0, 2, 0, 0]])


# if ywe have Nan
A = np.nan_to_num(A, 0)

print(A)

sparsity = 1.0 - (count_nonzero(A) / float(A.size))

print(sparsity)