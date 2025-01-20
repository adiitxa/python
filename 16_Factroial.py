#function calls itself

def factroial(n):
    if (n==0 or n==1) :
        return 1
    else :
        return n* factroial(n-1)
    
print(factroial(3))

