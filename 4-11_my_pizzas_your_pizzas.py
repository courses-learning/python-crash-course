# Make a list of 3x types of pizza and use a for loop to print
def print_list(pizzas):
    for pizza in pizzas:
        if pizza != pizzas[-1]:
            print(pizza, end=", ")
        else:
            print(pizza + ".")


pizzas = ['peperoni', 'hawian', 'meat feast']
# [:] required below to make a copy or lists remain linked
friends_pizzas = pizzas[:]
pizzas.append('hot and spicey')
friends_pizzas.append('tandoori chicken')
print(f"My friends favourite pizzas are: ", end="")
print_list(pizzas)
print(f"My favourite pizzas are: ", end="")
print_list(friends_pizzas)
