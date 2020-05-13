#Orthogonal Matrix:
# QT == Q^-1
# QQT == I


from numpy import array
from numpy import linalg
# from scipy import linalg


U = array([
   [-0.2298477, 0.88346102, 0.40824829],
   [-0.52474482, 0.24078249, -0.81649658],
   [-0.81964194, -0.40189603, 0.40824829]
])

VT = array([
   [-0.61962948, -0.78489445],
   [-0.78489445,  0.61962948]
])

BB = array([
   [-0.2298477],
   [-0.52474482],
   [-0.81964194]
])


# Standard Orthogonal Matrix
C = array([
   [1/3, 2/3, -2/3],
   [-2/3, 2/3, 1/3],
   [2/3, 1/3, 2/3]
])

# Matrix that produces a diagonal but is not normalized, therefore is not orthogonal
D = array([
   [1, 2, -2],
   [-2, 2, 1],
   [2, 1, 2]
])

print(U.dot(U.transpose()))
print(VT.dot(VT.transpose()))
# print(linalg.inv(C))

