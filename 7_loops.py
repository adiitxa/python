#loops in pyhthon
'''
1) for loop
2) while loop
3) for each loop
'''

'''keywords in python
1) continue
2) break
3) pass
4) else
'''

#while Loop in Pyhton
#for(i=1; i<=10; i++)

number = 1
while number>=0:
    print(number)
    number = number + 1

    if number == 5 :
        break


#for loop mostly used in list, sets, tuples, dictionry
list = [2, 4, 5, 6, 3, 10]
num = int(input("Enter number you want to found"))
for i in list:
    if i == num:
        print(F"number found {num}")
        break
    else :
        print("number not found!!")

#for loop using range
for i in range(5):
    print(i)

#for i in range(start, stop, increase):

#print even number through loop
for i in range(2, 101, 2):
    print(i)


#The enumerate() function provides the index and value in each iteration.
colors = ["red", "blue", "green"]
for index, color in enumerate(colors):
    print(f"Color {index + 1}: {color}")


#The zip() function combines two or more sequences.
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")



#nested For Loop
rows = 5 
for i in range(1, rows + 1):  # Outer loop for the number of rows
    for j in range(i):  # Inner loop for the number of stars in each row
        print("*", end="")  # Print stars on the same line
    print()  # Move to the next line
