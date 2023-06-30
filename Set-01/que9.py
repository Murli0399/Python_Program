def fibonacci(n):
    fibonacci_sequence = [0, 1] 

    for i in range(2, n):
        next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[:n]

n = 5
fibonacci_sequence = fibonacci(n)
print(fibonacci_sequence)
