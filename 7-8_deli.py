""" Fill a list with sandwich orders from user input as each made move to
another list and print full order when complete"""

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
    complete_order.append(sandwich)
    print(f"I made your {sandwich.lower()} sandwich.")

# End routine - print complete order
print('Your complete order is ready:')
for sandwich in complete_order:
    print(f'\t\t\t\t{sandwich} sandwich')
