#performing all operation on lsit
'''
1) Ordered: The elements in a list maintain the order they are added.
2) Mutable: You can modify elements, add, or remove items.
3) Heterogeneous: A list can store elements of different types.
4) Indexable and Slicable: Access elements by index and slice lists to create sublists.
4) Dynamic: Lists can grow or shrink as needed.
'''

'''
Agenda :
    1) Negative indexing
    2) in keyword in List
    3)Sliceing in list
'''


'''
1) append(x)	        Adds x to the end of the list.
2) extend(iterable)	    Adds all elements of an iterable to the list.
3) insert(i, x)	        Inserts x at index i.
4) remove(x)	        Removes the first occurrence of x.
5) pop([i])	            Removes and returns the element at index i (last if omitted).
6) clear()	            Removes all elements.
7) index(x)	            Returns the index of the first occurrence of x.
8) count(x)	            Returns the number of occurrences of x.
9) sort()	            Sorts the list in ascending order.
10) reverse()	        Reverses the order of the list.
11) copy()	            Returns a shallow copy of the list.
'''

list = [3, 4 , 5 , "aditya"]
print(list) 
print(list[-3])


#if you have give a negative index then first convert negative index to positive

print(list[len(list)-3])


#in keyword in lists
if "aditya" in list:
    print("yes")
else:
    print("no")


#by sliceing in list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(my_list[1:4])  # Output: [20, 30, 40]
print(my_list[:3])   # Output: [10, 20, 30]
print(my_list[::2])  # Output: [10, 30, 50]

#special all indexes like for loop
print("it skip 2 iteration :",my_list[1:9:2])  


#insert element direct via index
a = [1, 2, 3]
a[1] = 20
print(a)  # Output: [1, 20, 3]

#Performing all functions operation on list
newList = [1, 3 , 4 ,6 , 10]

#Append Function
newList.append(30)
print(newList)

#insert Function
newList.insert(3, 5)
print(newList)

#extend function
newList.extend([40, 77])
print(newList)

#Remove Function
newList.remove(77)
print(newList)

#pop function
newList.pop()
print(newList)

#index Function
index= newList.index(3)
print(index)

#count function
countItems = newList.count(3)
print(countItems)

#Reverse Function
newList.reverse()
print(newList)

#Sort Function
newList.sort()
print(newList)

#make Copy of List
copyOfList = newList.copy()
print(copyOfList)

#clear Function
newList.clear()
print(newList)


#concept of Nested List
nested_list = [[1, 2], [3, 4], [5, 6]] 
print(nested_list[1][1])

#using Len, Max, Min, Sum in List
print("\nCommon List Operations:")
numbers = [3, 1, 4, 1, 5]
print("Length of list:", len(numbers))
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Sum of elements:", sum(numbers))