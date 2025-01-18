#Dictionaries in python

myDict = {"name": "aditya", "age":"19", "year":"2nd"}
print(myDict)

#print Each Element in dictionaries
print(myDict["name"])

#key is no present still can't throw error
print(myDict.get("blood"))

#only print keys
print(myDict.keys(),"\n")

#with for
for key in myDict.keys():
    print(myDict[key])


#direct adding
myDict['post'] = "manager"

#For Values
print(myDict.values())

for key, values in myDict.items():
    print(f'{key} : {values}')

#dictionary methods :

