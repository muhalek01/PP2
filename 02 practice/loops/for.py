fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)  # apple, banana, cherry

# ---
for x in "banana":
    print(x)  # b, a, n, a, n, a


# Break after "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)  # apple, banana
    if x == "banana":
        break
# ---

# Break before "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)  # apple


# Continue (skip "banana")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)  # apple, cherry
