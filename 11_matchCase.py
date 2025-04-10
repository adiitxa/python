#this is just like switch case...But in switch case we use break statement but in python we dont use that 

a = int(input("enter a number"))


match a:

    case 0:
        print("given number is zero")
    case 1:
        print("given number is one")
    case _:
        print("inavlid choice !!!")


#You can use the pipe (|) symbol to match multiple values in one case.
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("It's a weekend!")
    case _:
        print("It's a weekday.")


#You can add conditions to patterns using if
value = 42

match value:
    case x if x < 10:
        print("Value is less than 10")
    case x if x % 2 == 0:
        print("Value is even")
    case _:
        print("Other value")

