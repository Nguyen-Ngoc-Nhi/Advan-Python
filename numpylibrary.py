import numpy as np

a1D = np.array([1, 2, 3, 4])
a2D = np.array([[1, 2], [3, 4]])
a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print('a1D = ', a1D)
print('a2D = ', a2D)
print('a3D = ', a3D)

# a = np.array([127, 128, 129], dtype=np.int8)
# print('a = ',a)

# aa = np.array([2, 3, 4], dtype=np.uint32)
# b = np.array([5, 6, 7], dtype=np.uint32)
# c_unsigned32 = aa - b
# print('unsigned c:', c_unsigned32, c_unsigned32.dtype)
# # unsigned c: [4294967293 4294967293 4294967293] uint32
# c_signed32 = aa - b.astype(np.int32)
# print('signed c:', c_signed32, c_signed32.dtype)
# # signed c: [-3 -3 -3] int64

# 1D array 
array = np.arange(10)
print('array = ', array)

array1 = np.arange(2, 10, dtype = float)
print('array1 = ', array1)

array2 = np.arange(2, 3, 0.1)
print('array2 = ', array2)

array3 = np.linspace(1., 4., 6)
print('array3 = ', array3)

# 2D array
array2D = np.eye(3)
print('2D array = \n', array2D)

array2D_ = np.eye(3, 5)
print('2D array = \n', array2D_)

arr = np.diag([1,2,3])
arr1 = np.diag([1, 2, 3], 1)
arr2 = np.array([[1, 2], [3, 4]])
arr3 = np.diag(arr2)

print('arr = \n', arr)
print('arr1 = \n', arr1)
print('arr2 = \n', arr2)
print('arr3 = \n', arr3)

arr4 = np.vander(np.linspace(0, 2, 5), 2)
arr5 = np.vander([1, 2, 3, 4], 2)
arr6 = np.vander((1, 2, 3, 4), 4)

print('arr4 = \n', arr4)
print('arr5 = \n', arr5)
print('arr6 = \n', arr6)

# Replicating, joining, mutating
a = np.array([1, 2, 3, 4, 5, 6])
b = a[:2]
b += 1
print('a =', a, '; b =', b)
# b is a variable, not array 
# if u want to create a new array, use np.copy
c = np.array([1, 2, 3, 4])
d = c[:2].copy()
d += 1
print('c = ', c, 'd = ', d)


