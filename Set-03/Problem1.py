num_tuples = int(input("Enter the number of tuples: "))
tuple_list = []

for _ in range(num_tuples):
    values = input("Enter values for the tuple (separated by spaces): ").split()
    tuple_values = tuple(values)
    tuple_list.append(tuple_values)

for n, a in tuple_list:
    print(f"{n} is {a} years old.")
