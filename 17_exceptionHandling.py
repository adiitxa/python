'''
An exception is an error that occurs during the execution of a program. When Python encounters an error, it raises an exception. If not handled, it stops the program execution and displays an error message.

Common Exception Types
1) SyntaxError     :       Code syntax is invalid.
2) NameError       :       Variable is not defined.


3) TypeError       :       Operation or function is applied to an object of inappropriate type.
4) ValueError      :       Function receives an argument of the right type but an inappropriate value.
5) IndexError      :       Index is out of range for a sequence.
6) KeyError        :       Accessing a key that does not exist in a dictionary.
7) ZeroDivisionError:      Division by zero.
'''

#here number can't be divided by zero
try:
   a= int(input("enter any number"))
   print(23/a)

except Exception as e :
    print(e)

except ValueError:
    print("Please enter a valid number.")

#if code is excuted without exception
else:
    print("successfully excuted")

#execute at any time
finally:
    print("finally block has been printed")


#raising Custom error
#programmer raise error


b = int(input("enter number for custom exception"))
if(a>5):
    raise ValueError("number is not acceptable")


'''
ArithmeticError	    Raised when an error occurs in numeric calculations
AssertionError	    Raised when an assert statement fails
AttributeError	    Raised when attribute reference or assignment fails
Exception	        Base class for all exceptions
EOFError	        Raised when the input() method hits an "end of file" condition (EOF)
FloatingPointError	Raised when a floating point calculation fails
GeneratorExit	    Raised when a generator is closed (with the close() method)
ImportError	        Raised when an imported module does not exist
IndentationError	Raised when indentation is not correct
IndexError	        Raised when an index of a sequence does not exist
KeyError	        Raised when a key does not exist in a dictionary
'''


