# чтение файла
with open("sample.txt", "r") as f:
    print(f.read())

# по строкам
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())
