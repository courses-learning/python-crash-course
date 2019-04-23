def invites(guests):
    # Generate and print out guest list invites
    for guest in guests:
        print(f"{guest.title()} you are invited to dinner at 1800hrs 24 Apr 2019.")


guests = ['bradley wiggins', 'albert einstein', 'winston churchill']
invites(guests)

decline = guests.pop(0)
print(f'\nUnfortunately {decline.title()} is unavailable...\n')
guests.append('bruce lee')
guests.insert(0, 'peter kay')

invites(guests)
print()

# Uninvite all but first 2 guests using pop
for i in range((len(guests)), 2, -1):
    uninvited = guests.pop(i-1)
    print(f"Sorry {uninvited.title()} you are uninvited - not enough room.")
print()

invites(guests)
