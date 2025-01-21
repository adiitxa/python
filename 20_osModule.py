import os

print(os.getcwd())

print(os.listdir("."))

os.chdir("__pycache__") 
print(os.getcwd())
os.chdir("..") 


os.mkdir("numpy")
os.rmdir("numpy")

#os.rename('da', 'dataSet')

path = os.path.join("D","python","programs")
print(path)

pathSplit = os.path.split("dic/python/numpy")
print(pathSplit)

print(os.path.exists("d/hello/python"))

print(os.path.isfile("customPackages.py"))
print(os.path.isdir("__pycache__"))

print(os.system("ls"))


#error Handling i python
try:
    os.remove('python.txt')
except FileNotFoundError:
    print("File not found!")