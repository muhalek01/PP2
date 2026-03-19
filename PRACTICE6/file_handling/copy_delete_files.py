import shutil
import os

# копирование
shutil.copy("sample.txt", "backup.txt")

# удаление
if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("File deleted safely")
else:
    print("File not found")
