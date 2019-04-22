# Make a list of 3 people you would invite to dinner & send personalised invite
def invites(guests):
    # Generate and print out guest list invites
    for guest in guests:
        print(f"{guest.title()} you are invited to dinner at 1800hrs 24 Apr 2019.")


guests = ['bradley wiggins', 'albert einstein', 'winston churchill']
invites(guests)

decline = guests.pop(0)
print(f'\nUnfortunately {decline.title()} is unavailable...\n')
guests.append('bruce lee')

invites(guests)
