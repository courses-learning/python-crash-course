def life_stage(age):
    if age < 2:
        return "a baby"
    elif age >= 2 and age < 4:
        return "a toddler"
    elif age >= 4 and age < 13:
        return "a kid"
    elif age >= 13 and age < 20:
        return "a teenager"
    elif age >= 20 and age < 65:
        return "an adult"
    elif age >= 65:
        return "an elder"
    else:
        return "not entering a valid age"


age = int(input("What is your age? "))
print(f"You are {life_stage(age)}")
