# Ask the user for a number and check if its a multiple of 10

flag = False
while flag is False:
    n = input("Please enter a number? ")
    flag = n.isdigit()

if int(n) % 10 == 0:
    print("Your number is a multiple of 10.")
else:
    print("Your number is not a multiple of 10.")
