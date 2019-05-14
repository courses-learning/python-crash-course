# Ask user how many guests & return conditional answer based on input

flag = False
while flag is False:
    guests = input("How many people are in your party? ")
    flag = guests.isdigit()

if int(guests) > 5:
    print("Please wait here to be seated.")
else:
    print("We have a table available. This way please.")
