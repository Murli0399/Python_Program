def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

number = 13
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
