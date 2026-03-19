import shutil

# перемещение файла
shutil.move("sample.txt", "test_dir/sample.txt")

# копирование обратно
shutil.copy("test_dir/sample.txt", "sample_copy.txt")
