import numpy as np

arr1 = np.array([1, 2, 3, 5])
arr2 =np.array([56, 54 , 76, 32 ])

#column wise apporach (top and bottom)
var1 = np.sum((arr1,arr2), axis = 0)
print("axis 0:",var1)

#Row wise approach
var2 = np.sum((arr1,arr2), axis = 1)
print("axis 1:",var2)

'''
1) Reamming Topics
2) Joining and Split 
3) Stack
4) machine Learning Functions
'''

