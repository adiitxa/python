'''
if condition:
    # Code to execute if the condition is True
else:
    # Code to execute if the condition is False
'''

age = 18

if age>=18:
    print("you are adult")

elif age <18:
    print("you are child")

else:
    print("hey, something went wrong !!!")


# nested if-else
number = 10

if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")


#Turnery Operator
#value_if_true if condition else value_if_false
age = 18

message = "vote" if age>=18 else "can't vote !!"
print(message)


#if-else with logical Operator

#and
age = 25
income = 50000

if age > 18 and income > 30000:
    print("You are eligible for the premium credit card.")
else:
    print("You are not eligible for the premium credit card.")

#or
day = "sunday"
if day=="sunday" or day == "saturday":
    print("holiday")
else:
    print("weekday !!!")

#not
rain = True
if not rain:
    print("go to walk")
else:
    print("dont go for walk");

#practice program
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(F"{year} is a leap year.")
else:
    print(F"{year} is not a leap year.")
