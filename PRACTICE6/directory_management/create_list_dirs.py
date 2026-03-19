import os

# создать папки
os.makedirs("test_dir/subdir", exist_ok=True)

# список файлов
print(os.listdir("."))

# текущая папка
print(os.getcwd())
