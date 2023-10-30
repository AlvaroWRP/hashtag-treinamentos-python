def persistence(number):
    if number < 10:
        return 0

    times_multiplied = 0
    product = 1

    while number >= 10:
        for digit in str(number):
            product *= int(digit)

        times_multiplied += 1
        number = product
        product = 1

    return times_multiplied

number = int(input('número: '))
print(persistence(number))
