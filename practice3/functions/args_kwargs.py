# args_kwargs.py
# 4 examples using *args and **kwargs

# Example 1: *args sum
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))

# Example 2: *args average
def average(*numbers):
    return sum(numbers) / len(numbers)

print(average(10, 20, 30))

# Example 3: **kwargs print info
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)

# Example 4: Combine *args and **kwargs
def display(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

display(1, 2, 3, name="Bob", city="London")
