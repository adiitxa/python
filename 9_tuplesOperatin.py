#tuples are immuatable

#create tuple with single element
tuple1 = (1, )

#tuple with multiple element
tuple2 = (1, "hello", 321, True)

print(tuple2)
print(tuple2[2])

#slicing
print(tuple2[1:4])

t = (1, 2, 2, 3, 4, 2)
print(t.count(2))