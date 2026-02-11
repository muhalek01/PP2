# return_values.py
# 4 examples returning different types

# Example 1: Return string
def full_name(first, last):
    return f"{first} {last}"

print(full_name("John", "Smith"))

# Example 2: Return tuple
def min_max(numbers):
    return min(numbers), max(numbers)

print(min_max([5, 10, 15]))

# Example 3: Return list
def double_numbers(numbers):
    return [n * 2 for n in numbers]

print(double_numbers([1, 2, 3]))

# Example 4: Return dictionary
def create_user(name, age):
    return {"name": name, "age": age}

print(create_user("Anna", 28))
