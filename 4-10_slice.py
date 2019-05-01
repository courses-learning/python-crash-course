# Use list slicing on earlier program
animals = ['elephant', 'rhino', 'hippo', 'lion', 'polar bear', 'giraffe']
for animal in animals:
    print(f"{animal.title()}s are very large animals.")
print("\nNone of the above would make suitable pets!!")

# Slicing a list, not terminating line on print statement & print list neatly
print(f"\nThe first 3 animals in the list are: ", end="")
print(*animals[:3], sep=", ")

# Looping through a slice
print(f"The last 3 animals in the list are: ", end="")
for animal in animals[len(animals)-3:]:
    if animal != animals[-1]:
        print(animal, end=", ")
    else:
        print(animal, end=".")
