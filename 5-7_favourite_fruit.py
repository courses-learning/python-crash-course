# Make a list of favourite fruits & write if statements to check if in list
def check(user_fruit):
    if user_fruit in fav_fruits:
        return True
    else:
        return False


fav_fruits = ["banana", "apple", "strawberry"]
user_fruit = input("Please enter your favourite fruit: ").lower()
if check(user_fruit) is True:
    print(f"We both like {user_fruit}s")
else:
    print("I don't like that....")
