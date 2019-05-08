""" Using code from book adapt to print bespoke message for people having
taken poll & not"""

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['jen', 'sarah', 'edward', 'phil', 'david', 'nicola']

for person in people:
    if person not in favourite_languages.keys():
        print(f"{person.title()} you have not yet taken the poll.")
    else:
        print(f"{person.title()} thank you for taking the poll.")
