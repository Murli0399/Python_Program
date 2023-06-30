def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

num1 = 5
num2 = 0
result = divide_numbers(num1, num2)
print(result) 
