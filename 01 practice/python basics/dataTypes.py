x = 5
print(f"{x} : {type(x)}")  # int

x = "Hello World"
print(f"{x} : {type(x)}")  # str

x = 20.5
print(f"{x} : {type(x)}")  # float

x = 1j
print(f"{x} : {type(x)}")  # complex

x = ["apple", "banana", "cherry"]
print(f"{x} : {type(x)}")  # list

x = ("apple", "banana", "cherry")
print(f"{x} : {type(x)}")  # tuple

x = range(6)
print(f"{x} : {type(x)}")  # range

x = {"name": "John", "age": 36}
print(f"{x} : {type(x)}")  # dict

x = {"apple", "banana", "cherry"}
print(f"{x} : {type(x)}")  # set

x = frozenset({"apple", "banana", "cherry"})
print(f"{x} : {type(x)}")  # frozenset

x = True
print(f"{x} : {type(x)}")  # bool

x = b"Hello"
print(f"{x} : {type(x)}")  # bytes

x = bytearray(5)
print(f"{x} : {type(x)}")  # bytearray

x = memoryview(bytes(5))
print(f"{x} : {type(x)}")  # memoryview

x = None
print(f"{x} : {type(x)}")  # NoneType
