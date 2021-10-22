
import shutil
import os
from sys import platform

def directory_work():
    print("Для создания директрии нажмите 1" + "\n" + "Чтобы удалить директорию нажмите 2")
    path = int(input())
    if path == 1:
        print("Введите полный путь до директории (включаю то, как вы хотите ее назвать):" + '\n')
        name = str(input())
        if "forUnix" not in name:
            print("Нельзя работать вне папки forUnix")
        else:
            os.mkdir(name)
    if path == 2:
        print("Введите полный путь до папки:" + '\n')
        name = str(input())
        if "forUnix" not in name:
            print("Нельзя работать вне папки forUnix")
        else:
            os.rmdir(name)


def file_work():
    print("Чтобы работать с файлом, введите полный путь до него, а потом в меню выберите действие:")
    path = str(input())
    if "forUnix" not in path:
        print("Нельзя работать вне папки forUnix")
    else:
        print(
            "Чтобы создать файл нажмите 1" + "\n" + "Чтобы Удалить файл нажмите 2" + "\n" + "Чтобы вывести данные из файла на экран нажмите 3" + "\n" + "Чтобы записать в файл строку нажмите 4" + "\n" + "Чтобы переименовать файл нажмите 5" + "\n" + "Чтобы скопировать файл нажмите 6")
        choice = int(input())
        if choice == 1:
            content = open(path, 'a+')
            content.close()
        elif choice == 2:
            os.remove(path)
        elif choice == 3:
            with open(path) as content:
                for line in content:
                    print(line)
        elif choice == 4:
            print("Введите строку для записи:")
            text = str(input())
            content = open(path, 'a+')
            content.write(text)
            content.close()
        elif choice == 5:
            print("Введите полный путь с новым названием")
            text1 = str(input())
            os.rename(path, text1)
        elif choice == 6:
            print("Введите новый полный путь")
            text2 = str(input())
            shutil.copyfile(path, text2)


while True:
    print("Вы находитесь в программе 'простейший файловый менеджер' для работы создайте свою директорию 'forUnix'" + '\n'
        "Для создания или удаления директории нажмите 1" + '\n' + "Нажмите 2 для вызова командной строки и работы вручную" + '\n' + "Для всей работы с файлами нажмите 3")
    inp = int(input())
    if inp == 1:
        directory_work()
    elif inp == 2:
        if platform == "linux" or platform == "linux2":
            os.system('gnome-terminal')
        else:
            os.system(
                '"C:\WINDOWS\system32\cmd.exe"')  # командная строка
    elif inp == 3:
        file_work()