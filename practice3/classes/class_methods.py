# class_methods.py

# Example 1
class Dog:
    def bark(self):
        return "Woof"

print(Dog().bark())

# Example 2
class Calculator:
    def add(self, a, b):
        return a + b

print(Calculator().add(5, 3))

# Example 3
class Greeting:
    def say_hello(self, name):
        return f"Hello {name}"

print(Greeting().say_hello("Anna"))

# Example 4
class Counter:
    def increment(self, value):
        return value + 1

print(Counter().increment(10))
