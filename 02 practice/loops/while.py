i = 1
while i < 6:
    print(i)  # 1, 2, 3, 4, 5
    i += 1

print("---")

# break
i = 1
while i < 6:
    print(i)  # 1, 2, 3
    if i == 3:
        break
    i += 1

print("---")

# continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)  # 1, 2, 4, 5, 6

print("---")

# else
i = 1
while i < 6:
    print(i)  # 1, 2, 3, 4, 5
    i += 1
else:
    print("i is no longer less than 6")  # i is no longer less than 6
