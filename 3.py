import os
path = os.getcwd()
print("Текущая дирректория %s" % path)

path = "/кк"
try:
    os.mkdir(path)
except OSError:
    print("Создать директорию %s не удалось" % path)
else:
    print("Успешно создана директория %s " % path)