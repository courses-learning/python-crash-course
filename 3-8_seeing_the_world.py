# Create & print list of places to visit
locs = ['great barrier reef', 'mount everest', 'carribean', 'pyramids']
print(locs)
# Dont modify list using sorted
print(sorted(locs))
# Show still in original order
print(locs)
# print in reverse without modifying
print(sorted(locs, reverse=True))
# Show still in original order
print(locs)
# Use reverse to change order of list
locs.reverse()
print(locs)
# Use reverse to change back order of list
locs.reverse()
print(locs)
# Use sort to store list alphabetically
locs.sort()
print(locs)
# Use sort to store list reverse alphabetically
locs.sort(reverse=True)
print(locs)
