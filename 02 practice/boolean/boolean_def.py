def myFunction():
    return True

print(myFunction())  # True

if myFunction():
    print("YES!")  # YES!
else:
    print("NO!")

# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))  # True
