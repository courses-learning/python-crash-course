# Store a name with whitespace within a variable. Print using strip functions.
name = '\tDAVID   '
print(f"{name} - No Stripping")
print(f"{name.lstrip()} - Left Strip")
print(f"{name.rstrip()} - Right Strip")
print(f"{name.strip()} - Strip")
