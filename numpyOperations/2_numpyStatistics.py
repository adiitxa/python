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

#mathmatical Operations
array

print("\n dot product : ", np.dot(arr_1, arr_2)) #dot product of all
print("matmul function ", np.matmul(arr_1, arr_2))

#Broadcasting 
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])

result = arr1 + arr2  # arr2 is broadcasted across rows
print(result)


#Stastics Concepts in numpy
one1 = np.array([2, 3, 5, 7, 6])
meanValue = np.mean(one1)
print("\n",meanValue)

two2 =np.array([1, 2, 3 ,5, 6, 9])
medianValue = np.median(two2)
print(medianValue)

