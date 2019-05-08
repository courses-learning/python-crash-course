# Use a dictionary to make a glossary of programming words learnt & meaning
must_remember = {
    ".items()": "use after 'for key, value in' loop to iterate over dictionary keys & values",
    ".keys()": "use to loop through keys only - also default behaviour",
    "set()": "use around a list to create a set of unique items",
    "sorted": "Use with list to return sorted list - can be used with .keys() etc",
}

for key, value in must_remember.items():
    print(f"{key} : {value}")
