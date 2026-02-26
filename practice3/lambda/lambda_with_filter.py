# lambda_with_filter.py

numbers = [5, 10, 15, 20, 25]

# Example 1: even numbers
print(list(filter(lambda x: x % 2 == 0, numbers)))

# Example 2: numbers > 15
print(list(filter(lambda x: x > 15, numbers)))

# Example 3: numbers < 20
print(list(filter(lambda x: x < 20, numbers)))

# Example 4: odd numbers
print(list(filter(lambda x: x % 2 != 0, numbers)))
