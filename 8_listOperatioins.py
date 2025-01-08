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
append(x)	        Adds x to the end of the list.
extend(iterable)	Adds all elements of an iterable to the list.
insert(i, x)	    Inserts x at index i.
remove(x)	        Removes the first occurrence of x.
pop([i])	        Removes and returns the element at index i (last if omitted).
clear()	            Removes all elements.
index(x)	        Returns the index of the first occurrence of x.
count(x)	        Returns the number of occurrences of x.
sort()	            Sorts the list in ascending order.
reverse()	        Reverses the order of the list.
copy()	            Returns a shallow copy of the list.
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
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  # Output: [20, 30, 40]
print(my_list[:3])   # Output: [10, 20, 30]
print(my_list[::2])  # Output: [10, 30, 50]
print(my_list[::3])  # Output: [10, 30, 50]

