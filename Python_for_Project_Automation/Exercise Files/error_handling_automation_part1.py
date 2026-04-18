# This code demonstrates error handling in Python using try-except blocks.
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("The result is:",result)
except ValueError:
    print("You must enter a valid integer value.")
except ZeroDivisionError:
    print("You cannot divide this number by zero.")