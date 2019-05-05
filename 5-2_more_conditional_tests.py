# More conditional tests inc >= & <=, and, or, items in lists

pizzas = ['peperoni', 'hawian', 'meat feast']
friend_fav_pizza = input("what is your friends favourite pizza? ").lower()
my_fav_pizza = input("what is your favourite pizza? ").lower()

if my_fav_pizza in pizzas and friend_fav_pizza in pizzas:
    print("We serve both of your favourite pizzas")
elif my_fav_pizza not in pizzas and friend_fav_pizza not in pizzas:
    print("We don't have any pizzas you would like")
else:
    print("We only serve one of your favourite pizzas")

no = int(input("How many pizzas would you like to order? "))
if no > 5:
    print("sorry too many...")
elif no <= 5:
    print("Ok please wait...")
else:
    print("Sorry thats not what I asked.")
