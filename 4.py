import os
directory = "C:\Users\Администратор\Desktop\Прог"
files = []
files += os.listdir(directory)
print(files)