import numpy as np

arr1 = np.array([2, 3, 5, 7, 6])

for i in arr1 :
    print(i)

print()
#iterating array with function
for i in np.nditer(arr1, flags=['buffered'], op_dtypes=['S']):
    print(i)

print()
#enumrate function in numpy
for i,d in np.ndenumerate(arr1):
    print("index :",i, "data :", d)


#copy and Views

#copy creats new array in new Location
copy = np.copy(arr1)
print("\n Copied Array :",copy)

#view creats only new insatnce varible but loication is same
view = arr1.view()
print("\n View Function Array :", view)


#Stastics and Linear Algebra Concepts in numpy
one1 = np.array([2, 3, 5, 7, 6])
meanValue = np.mean(one1)
print("\n mean value of Array :",meanValue)

two2 =np.array([1, 2, 3 ,5, 6, 9])
medianValue = np.median(two2)
print("\n median value of Array :",medianValue)



