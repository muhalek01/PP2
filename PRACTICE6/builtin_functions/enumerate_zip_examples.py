names = ["Ali", "Dana", "Omar"]
scores = [90, 85, 88]

# enumerate
for i, name in enumerate(names):
    print(i, name)

# zip
for name, score in zip(names, scores):
    print(name, score)

# sorted
print(sorted(scores))

# type conversion
x = "123"
print(int(x), type(int(x)))
