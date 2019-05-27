# Use ex 7-8 code to print a message saying no pastrami & remove from list

sandwich_orders = []
complete_order = []
order = ''

# Take order
while order.lower() != 'e':
    order = input('Please enter your sandwich order ("e" to exit): ')
    if order != 'e':
        sandwich_orders.append(order.title())

# Move sandwiches to different completed list and print message for each made
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich.lower() == 'pastrami':
        print('Sorry we have run out of pastrami.')
    else:
        complete_order.append(sandwich.lower())
        print(f"I made your {sandwich.lower()} sandwich.")

# End routine - print complete order
print('Your complete order is ready:')
for sandwich in complete_order:
    print(f'\t\t\t\t{sandwich} sandwich')
