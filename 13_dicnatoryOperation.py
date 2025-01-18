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

myDict1 = {23:2, 24:1, 25:3}
myDict2 = {1 : 12, 2: 13}

myDict1.update(myDict2)
print(myDict1)

myDict1.pop(24)
print(myDict1)

myDict2.popitem()
print(myDict2)

myDict.clear()
print(myDict)

#deleting key value pairs
del myDict1[23]
print(myDict1)

#checking Existance
print('name' in myDict1)

#Advance python concepts
#nested dictionary

nested_dict = {

    'dict1' :{"app":"insta", "foll":23},
    'dict2' :{"app": "WhatsApp", "foll":65}
}

print(nested_dict['dict1']['app'])