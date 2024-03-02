import numpy as np

print("1-dimensional ARRAY")
# Initialize a one-dimensional array with integer data type
arr = np.array([1, 2, 3, 4, 5, 6], dtype=int)

#Khởi tạo mảng một chiều với kiểu dữ liệu mặc định
arr1 = np.array([1,2,3,4,5,6])

print(arr)
print(arr1)

print('\n----------------------------------------------')

print('\n2-dimensional ARRAY')
arr2 = np.array([(4,5,6), (1,2,3)], dtype = int)

print(arr2)

print('\n----------------------------------------------')

print('\n3-dimensional ARRAY')
arr3 = np.array(([(2,4,0,6), (4,7,5,6)],
                 [(0,3,2,1), (9,4,5,6)],
                 [(5,8,6,4), (1,4,6,8)]), dtype = int)
print(arr3)

print('\n----------------------------------------------')

print('\nAvailable ARRAY')
# Tạo mảng hai chiều các phần tử 0 với kích thước 3x4
arr0_3x4 = np.zeros((3,4), dtype = int)
# Tạo mảng 3 chiều các phần tử 1 với kích thước 2x3x4
arr1_2x3x4 = np.ones((2,3,4), dtype = int)
# Tạo mảng với các phần tử từ 1 - 6 với bước nhảy là 2
arr1_6_2 = np.arange(1,7,2)
# Tạo mảng 2 chiều các phần tử 5 với kích thước 2x3
arr5_2x3 = np.full((2,3),5)
# Tạo ma trận đơn vị với kích thước là 4x4
arr4x4 = np.eye(4, dtype=int)
# Tạo ma trận các phần tử ngẫu nhiên với kích thước 2x3
arr_random_2x3 = np.random.random((2,3))
print(arr0_3x4)
print('----------------------------------------------')
print(arr1_2x3x4)
print('----------------------------------------------')
print(arr1_6_2)
print('----------------------------------------------')
print(arr5_2x3)
print('----------------------------------------------')
print(arr4x4)
print('----------------------------------------------')
print(arr_random_2x3)

print('\n----------------------------------------------')

print('\nEdit ARRAY')
print("Kiểu dữ liệu của phần tử trong mảng:", arr3.dtype)
print("Kích thước của mảng:", arr3.shape)
print("Số phần tử trong mảng:", arr3.size)
print("Số chiều của mảng:", arr3.ndim)

print("arr[2]=", arr[2])
print("arr2[1:2]=", arr1[1,2])
print("arr3[1,2,3]=", arr2[1,1,3])
print("arr[0:3]=", arr[0:3])
print("arr2[:,:1]=", arr1[:,:2])






