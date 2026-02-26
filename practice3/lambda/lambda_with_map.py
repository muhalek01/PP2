# lambda_with_map.py

numbers = [1, 2, 3, 4]

# Example 1: multiply by 2
print(list(map(lambda x: x * 2, numbers)))

# Example 2: convert to string
print(list(map(lambda x: str(x), numbers)))

# Example 3: square numbers
print(list(map(lambda x: x ** 2, numbers)))

# Example 4: add 10
print(list(map(lambda x: x + 10, numbers)))
