#tuples are immuatable

'''
count(value)	        Counts occurrences of value.
index(value)	        Returns the first index of value.
len()	                Returns the length of the tuple.
+	                    Concatenates tuples.
*	                    Repeats the tuple.
in	                    Checks for membership.
for loop	            Iterates through tuple elements.
sorted()	            Returns a sorted list of tuple elements.
'''

#create tuple with single element
tuple1 = (1, )

#tuple with multiple element
tuple2 = (1, "hello", 321, True)

print(tuple2)
print(tuple2[2])

#slicing
print(tuple2[1:4])

t1 = (1, 2, 2, 3, 4, 2)
print(t1.count(2))

t2 = (10, 20, 30, 40)
print(t2.index(30))

#concact 2 list
print(t1 + t2)  

#list multiply 3 copy
print(t1 * 3)

#nested tuples
nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple[1])  
print(nested_tuple[1][0])  
