# Using program from 6-1 create list of dictionaries & print peoples info
a0001 = {
    "first": "daniel",
    "last": "smith",
    "age": 25,
    "city": "durham",
}

a0002 = {
    "first": "david",
    "last": "scott",
    "age": 34,
    "city": "manchester",
}

a0003 = {
    "first": "matthew",
    "last": "black",
    "age": 40,
    "city": "glasgow",
}

people = [a0001, a0002, a0003]

for id in people:
    print(id["first"].title(), end=" ")
    print(id["last"].title())
    print(id["age"])
    print(id["city"].title())
    print()
