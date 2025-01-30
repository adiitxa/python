'''
w = wirte : write()
r = read : read()
a = append : write()

r+ : read and write
'''

f = open('22_practiceFile.txt','r')
text = f.read()
print(text)
f.close()

f2 = open('22_practiceFile.txt', 'w')
text = f2.write("\n hello, Aditya")
f2.close()



#with Enclousare 
with open('22_practiceFile.txt', 'r+') as file1:
    file1.write("\n ooh bosss")

