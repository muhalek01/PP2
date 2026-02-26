# math.py

import math
import random

print("BUILT-IN FUNCTIONS")
print("Min:", min(3, 7, 1))
print("Max:", max(3, 7, 1))
print("Absolute:", abs(-5))
print("Round:", round(3.6))
print("Power:", pow(2, 3))

print("\nMATH MODULE")
print("Square root:", math.sqrt(16))
print("Ceil:", math.ceil(2.3))
print("Floor:", math.floor(2.9))
print("Pi:", math.pi)
print("Euler number:", math.e)

print("\nRANDOM MODULE")
print("Random float:", random.random())
print("Random integer:", random.randint(1, 10))

names = ["Ali", "Dana", "Madi"]
print("Random choice:", random.choice(names))

random.shuffle(names)
print("Shuffled list:", names)