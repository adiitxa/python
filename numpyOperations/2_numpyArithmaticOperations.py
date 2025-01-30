import numpy as np

#Arithmatic Functions on Array
arr_1 = np.array([1, 4, 6])
arr_2 = np.array([5, 4, 2])


print("\n Addition",arr_1 + arr_2) # we can also use add() function
print("\n multiply :", arr_1*arr_2)
print("\n Square Function :", arr_1**2)
print("\n modulas :", arr_1%arr_2)
print("\n Reciprocal :", np.reciprocal(arr_1))

var = 3
print("\n adding a varible to array: ",arr_1 + var)

print("\n array concat :",np.concatenate((arr_1, arr_2)))

print()

arr20 = np.array([[1, 4], [2, 5]])
arr21 = np.array([[5, 4]])

print("vertical concate :\n",np.concatenate((arr20, arr21), axis=0))

#mathmatical Operations
arr3 = np.array([34, 54, 78, 90])
print("\n maximum value :", np.max(arr3))
print("\n minimum value:",np.min(arr3))

print("\n dot product : ", np.dot(arr_1, arr_2)) #dot product of all
print("\n matmul function ", np.matmul(arr_1, arr_2))


#Broadcasting 
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])

result = arr1 + arr2  # arr2 is broadcasted across rows
print("\n",result)


#fancy indexig
arr = np.array([10, 20, 30, 40, 50])
indices = np.array([0, 2, 4])
print(arr[indices])

#boolean Masking
arr = np.array([1, 2, 3, 4, 5, 6])
mask = arr % 2 == 0  

print(arr[mask])


