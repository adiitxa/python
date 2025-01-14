'''
1) Unordered Collection:
Sets do not maintain the order of elements. This means you cannot access elements by index like in lists or tuples.

2) Unique Elements:
A set automatically removes duplicate elements, ensuring all elements in the set are unique.

3) Mutable:
While the set as a whole is mutable, the elements within it must be immutable.

4) No Indexing or Slicing:
Since sets are unordered, indexing and slicing are not supported.
'''

'''
1) add()	                Adds an element to the set.
2) clear()	                Removes all elements from the set.
3) copy()	                Returns a shallow copy of the set.
4) difference()	            Returns the difference between sets.
5) intersection()	        Returns common elements between sets.
6) isdisjoint()	            Checks if two sets are disjoint.
7) issubset()	            Checks if a set is a subset of another.
8) issuperset()	            Checks if a set is a superset of another.
8) pop()	                POP elememt
10) remove()	            Removes a specified element (raises an error if not found).
11) symmetric_difference()	Returns symmetric difference of two sets.
12) union()	                Returns the union of sets.
13) update()	            Adds elements from another set or iterable.

'''

#Duplicate Element only at once
my_set = {1, 2 , 2 , 3, 4}
print(my_set)

#set using set constructur
another_set = set([1, 2, 3, 3, 4, 8, 9])  
print(another_set)

#update Function
updateSet = another_set.update(my_set)
print("updated :", updateSet)

my_set.add(13)
print(my_set)

#remove element and Rise error if Element not present
my_set.remove(2)
print(my_set)

#remove element and Dont Rise the error
my_set.discard(10)
print(my_set)


# IMPORTANT METHODS OF SETS

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
print(set_a.union(set_b))  # {1, 2, 3, 4, 5, 6}

# Intersection
print(set_a.intersection(set_b))  # {3, 4}

# Difference
print(set_a.difference(set_b))  # {1, 2}

# Symmetric Difference
print(set_a.symmetric_difference(set_b))  # {1, 2, 5, 6}


#superset 
print(set_b.issuperset(set_a))

#subset
print(set_a.issubset(set_b))

#disjoint
print(set_a.isdisjoint(set_b))


