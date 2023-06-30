def factorial(number):
    if number == 0:
        return 1

    else:
        return number * factorial(number - 1)

number = 6
ans = factorial(number)
print("Factorial of", number, "is", ans)
