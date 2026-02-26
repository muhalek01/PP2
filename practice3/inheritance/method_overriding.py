# method_overriding.py

# Example 1
class Animal:
    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

# Example 2
class Bird:
    def move(self):
        return "Flying"

class Penguin(Bird):
    def move(self):
        return "Swimming"

# Example 3
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def area(self):
        return 10

# Example 4
class Person:
    def role(self):
        return "Person"

class Teacher(Person):
    def role(self):
        return "Teacher"
