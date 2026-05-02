print(bool("Hello"))  # True
print(bool(15))       # True

x = "Hello"
y = 15
print(bool(x))  # True
print(bool(y))  # True
print(bool("abc"))  # True
print(bool(123))    # True
print(bool(["apple", "cherry", "banana"]))  # True

print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False
print(bool(""))     # False
print(bool(()))     # False
print(bool([]))     # False
print(bool({}))     # False

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))  # False
