# Prompt users for name & dream vacation then stoe in a dictionary

name = 'x'
loc = 'x'
dreams = {}

print('Just press enter at anytime to end the poll and see results.')

# While loop for main poll
while name != '' and loc != '':
    name = input('Enter persons name: ')
    if name == '':
        break
    loc = input(f"Where is {name.title()}'s dream holiday destination: ")
    if loc == '':
        break
    # Add to dictionary with name for key & location for value
    dreams[name.title()] = loc.title()

# Iterate through results in dict and dislay
print('\nResults of poll as follows:')
for name, holiday in dreams.items():
    print(f"\t\t\t\t{name}'s dream holiday is {holiday}.")
