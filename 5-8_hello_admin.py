""" Make a list of 5 or more usernames + a special admin. Print grreting to
each & bespoke to admin user"""

users = ["David11664", "JoeW5", "Nicola83P", "Admin", "Luke22"]
for user in users:
    print(f"Hello {user}", end="")
    if user == "Admin":
        print(" - would you like to see a status report?")
    else:
        print()
