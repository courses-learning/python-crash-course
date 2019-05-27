# Write a loop that prompts user for toppings until 'quit' is entered

# Set initial variables
pizza = ['cheese']
topping = ''

# User inputs until 'quit' entered
while topping != 'quit':
    topping = input('\nPlease enter your required topping: ')
    if topping == '':
        print('Please enter a topping')
        continue
    elif topping.lower() == 'quit':
        break
    else:
        pizza.append(topping.lower())
        print(f'{topping.title()} has been added to your pizza')

print('\nYour pizza is complete:')
for topping in pizza:
    print(f'\t\t\t{topping.title()}')
