# Store a persons name in a variable & then print in lower, upper & title cases
def show_str(name, case, i):
    print(f'Stored name in {case}: ', end='')
    if i == 0:
        print(name.upper())
    elif i == 1:
        print(name.lower())
    else:
        print(name.title())


name = 'david'
cases = ['upper', 'lower', 'title']
for i in range(3):
    show_str(name, cases[i], i)
