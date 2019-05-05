# Write a series of conditional tests. Print a statement describing & result


def test(my_car, my_num, car_guess, num_guess):
    # conduct tests ==,<,>,!= and print results for str & num
    print(f"Test: {my_car} == {car_guess} is ", end="")
    print(my_car == car_guess)
    print(f"Test: {my_num} == {num_guess} is ", end="")
    print(my_num == num_guess)

    print(f"Test: {my_car} > {car_guess} is ", end="")
    print(my_car > car_guess)
    print(f"Test: {my_num} > {num_guess} is ", end="")
    print(my_num > num_guess)

    print(f"Test: {my_car} < {car_guess} is ", end="")
    print(my_car < car_guess)
    print(f"Test: {my_num} < {num_guess} is ", end="")
    print(my_num < num_guess)

    print(f"Test: {my_car} != {car_guess} is ", end="")
    print(my_car != car_guess)
    print(f"Test: {my_num} != {num_guess} is ", end="")
    print(my_num != num_guess)


car_guess = input("What do you think my car is? ")
num_guess = input("What do you think my number is? ")

test("Land Rover Discovery", 7, car_guess.title(), int(num_guess))
