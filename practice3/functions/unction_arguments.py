# function_arguments.py
# 4 examples of different argument types

# Example 1: Default argument
def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(5, 3))

# Example 2: Positional arguments
def subtract(a, b):
    return a - b

print(subtract(10, 4))

# Example 3: Keyword arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="John")

# Example 4: Mixed arguments
def order(item, quantity=1):
    print(f"Ordered {quantity} {item}(s)")

order("Book")
order("Pen", 3)
