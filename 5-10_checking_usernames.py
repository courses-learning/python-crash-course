# Create a program that simulates how websites ensure all have unique usernames


def get_new():
    new = input("Hello new user. Please enter your username: ").upper()
    while new in usernames:
        new = input("Sorry that username is taken. Please select another: ").upper()
    return new


usernames = ["DAVID1664", "JOEW5", "NICOLA83P", "ADMIN", "LUKE22"]

new = get_new()
usernames.append(new)
print("\nList of current users:")
for user in usernames:
    print(user)
