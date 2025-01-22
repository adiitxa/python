def function_read():
    #local varible
    x = 10
    print(x)


#global variable
a = 10

def function_two():
    global a
    a=a+10
    print(a)

function_two()
function_read()