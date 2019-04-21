""" Think of your favourite mode of transpot. Make a list and use this to print
statements"""
vehs = [
    {'type': 'car', 'name': 'Ferrari'},
    {'type': 'camper', 'name': 'VW California Ocean'},
    {'type': 'other', 'name': 'Apache Helicopter'}
]

for item in vehs:
    if item["type"] == 'car':
        print(f'My favourite car would be a {item["name"]}')
    elif item["type"] == 'camper':
        print(f'If I had the money I would buy a {item["name"]}')
    elif item["type"] == 'other':
        print(f'The ultimate would be to own an {item["name"]}')
