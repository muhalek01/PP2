# multiple_inheritance.py

# Example 1
class A:
    pass

class B:
    pass

class C(A, B):
    pass

# Example 2
class Father:
    def skill1(self):
        return "Driving"

class Mother:
    def skill2(self):
        return "Cooking"

class Child(Father, Mother):
    pass

# Example 3
class X:
    pass

class Y:
    pass

class Z(X, Y):
    pass

# Example 4
class Writer:
    def write(self):
        return "Writing"

class Speaker:
    def speak(self):
        return "Speaking"

class Person(Writer, Speaker):
    pass
