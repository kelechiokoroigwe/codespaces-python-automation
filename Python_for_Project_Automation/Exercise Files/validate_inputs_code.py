import pyinputplus as pyip

print("\nEXAMPLE 1")

# uncomment the following line of code and fill in 
result = pyip.inputInt(prompt="How many store bags do you need for your groceries? ", min=0)

# uncomment the following line of code
print("\nYou will use", result, "store bags.")

print("\nEXAMPLE 2")

# uncomment the following line of code and fill in  
result = pyip.inputMenu(["Red", "Blue", "Green"], prompt="What color marker do you want? ")

# uncomment the following line of code
print("\nYou have chosen a", result, "marker.")

print("\nEXAMPLE 3")

# uncomment the following line of code and fill in 
result = pyip.inputEmail(prompt="What is your email address? ")

# uncomment the following line of code
print("\nThe email you entered:", result)