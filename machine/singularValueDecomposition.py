# Singular Value Decomposition w/ SciPy
from numpy import array
# from scipy.linalg import svd
# from scipy.linalg import inv
from scipy.linalg import *

##

# A = array([
#    [1.1, 1.0, 0.9, 1.0],
#    [1.0, 1.1, 1.0, 0.9]])

A = array([
   [1, 2],
   [3, 4],
   [5, 6]])

B = array([
   [2, 3],
   [1, 5]
])
   
# print("input \n", A)

# print("column \n", A[:,3])
##

U, s, VT = svd(A, full_matrices= True)
print("U \n", U)
print("S \n", s)
print("VT \n", VT)