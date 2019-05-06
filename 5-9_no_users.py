# Use previous exercise with no users and check if list empty

users = []
if users:
    for user in users:
        print(f"Hello {user}", end="")
        if user == "Admin":
            print(" - would you like to see a status report?")
        else:
            print()
else:
    print("We have no users.....")
