# init_method.py

# Example 1
class Person:
    def __init__(self, name):
        self.name = name

p = Person("John")
print(p.name)

# Example 2
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c = Car("Toyota", 2022)
print(c.brand, c.year)

# Example 3
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Example 4
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
