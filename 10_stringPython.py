string1 = '''hello''' #multiline string

str1 = "hello"
str2 = "world"

#string Concact
print(str1 + str2)

# 1) Case Conversion
stringOne = "hello from python"
print(stringOne.capitalize()) #only first character of string

print(stringOne.title()) #capatalize the each 1st letter of string


print(stringOne.upper()) #all charcter to upper
print(stringOne.lower()) #all character to lower
print(stringOne.swapcase()) #case swapping


# 2) Alignment Method
s = "hello"
print(s.center(10, '-'))  
print(s.ljust(10, '-')) 
print(s.rjust(10, '-'))  


# 3) check Methods check whearther true or false
s2 = "hello"
print(s2.isalpha())
print(s2.isdigit())
print(s2.isalnum())

s3= "   "
print(s3.isspace())

s4 = "hello"
print(s4.islower())

s5 = "HELLO"
print(s5.isupper())

s6 = "hello world"
print(s6.istitle())



#modify methods
s7= "hello world"
print(s7.replace("world", "Python")) 

s8 = "  hello  "
print(s8.strip()) 

s9 = "  hello  "
print(s9.lstrip())

s10 = "  aditya   "
print(s10.rstrip())



#searching and counting

#find index of G first occurance
s11= "Aditya Gaikwad"
print(s11.find("Gaikwad"))

#find last element of substring
s12 = "hello world"
print(s12.rfind("l"))
#print(s.rfind("l", 0, 5))  we can also specify the index

s13 = "banana"
print(s.count("a"))  
#Splitting and Joining

s14 = "hello world"
print(s14.split())  # Output: ["hello", "world"]

s15 = "hello world"
print(s15.rsplit())  # Output: ["hello", "world"]

s16 = "hello\nworld"
print(s16.splitlines())  # Output: ["hello", "world"]

s17 = "-"
print(s17.join(["hello", "world"]))  # Output: "hello-world"



