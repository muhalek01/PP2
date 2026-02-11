# super_function.py

# Example 1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

# Example 2
class Vehicle:
    def start(self):
        return "Engine started"

class Car(Vehicle):
    def start(self):
        return super().start() + " - Car ready"

# Example 3
class A:
    def greet(self):
        return "Hello"

class B(A):
    def greet(self):
        return super().greet() + " World"

# Example 4
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")
