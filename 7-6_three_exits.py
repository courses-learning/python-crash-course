# Ex 7-5 with conditional 'quit' added


# Func takes an int as age returning int for cost of ticket
def get_cost(age):
    if age < 3:
        return 0
    elif age < 13:
        return 10
    else:
        return 15


no_tickets = ''
total = 0

# Check input is a number and get no of req tickets
while no_tickets.isdigit() is False:
    no_tickets = input('How many tickets would you like? ')
    if no_tickets.lower() == 'quit':
        print('You have selected quit. Goodbye.')
        no_tickets = 0
        break

# get age for each ticket, check no is inputted and keep running total
for i in range(0, int(no_tickets)):
    age = ''
    while age.isdigit() is False:
        age = input(f'What age is ticket {i+1}: ')
    cost = get_cost(int(age))
    print(f'This ticket will cost £{cost}')
    total += cost

print(f'Total cost of all tickets: £{total}')
