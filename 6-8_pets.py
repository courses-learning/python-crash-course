"""Make multiple dict where dict name is pet name. Store all in a list of
dicts and print all details for each"""

snowy = {
    'name': 'snowy',
    'type': 'cat',
    'breed': 'ragdoll',
    'colour': 'white',
    'owner': 'david & nicola'
}

jake = {
    'name': 'jake',
    'type': 'dog',
    'breed': 'labrador',
    'colour': 'black',
    'owner': 'john & carole'
}

rosie = {
    'name': 'rosie',
    'type': 'dog',
    'breed': 'spaniel',
    'colour': 'white & brown',
    'owner': 'daniel'
}

beth = {
    'name': 'beth',
    'type': 'dog',
    'breed': 'collie',
    'colour': 'white & brown',
    'owner': 'susan & david'
}

pets = [snowy, jake, rosie, beth]
for pet in pets:
    print(f"\n{pet['name'].title()} is a {pet['breed']} {pet['type']}.", end='')
    print(f" It's {pet['colour']} and owned by {pet['owner'].title()}")
