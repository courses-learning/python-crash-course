""" Make a dictionary containing 3 major rivers & country - print sentance
using loop and seperate lists for keys & values"""

rivers = {
    "nile": "egypt",
    "thames": "england",
    "amazon": "brazil",
    "tyne": "england",
}

for river, country in rivers.items():
    print(f"The river {river.title()} is located in {country.title()}")

print("\nAll rivers alphabetically:")
for river in sorted(rivers.keys()):
    print(f"\t{river.title()}")

print("\nAll unique countries alphabetically:")
for country in sorted(set(rivers.values())):
    print(f"\t{country.title()}")
