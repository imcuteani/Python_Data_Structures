from numpy import *
from numpy.matrixlib.defmatrix import matrix 

matrix_a = array([['January', 1,7,14,21,28], ['February', 2, 9, 18,25,30],['March', 3, 10,17,24,31]])

matrix_shape = reshape(matrix_a,(3,6))
print(matrix_shape)

# Addition in Matrix

print(matrix_shape[1])

print(matrix_a[2])

add = append(matrix_a, [['April', 4, 11, 17, 24, 31]])

print(add)