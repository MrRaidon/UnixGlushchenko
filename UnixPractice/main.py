
import shutil
import os
from sys import platform
import sys
dirname = "forUnix"
tecdir=os.getcwd()
def directory_work():
    print("Для создания директрии нажмите 1" + "\n" + "Чтобы удалить директорию нажмите 2")
    path = int(input())
    if path == 1:
        print("Введите название новой директории")
        na = str(input())
        name = os.getcwd() +"/"+dirname + "/" + na
        if dirname not in name:
            print("Нельзя работать вне рабочей папки")
        else:
            os.mkdir(name)
            os.chdir(os.getcwd()+"/"+dirname+"/"+na)

    if path == 2:
        print("Введите название директории, которую хотите удалить:")
        name = os.getcwd() +"/"+dirname+"/"+str(input())
        if dirname not in name:
            print("Нельзя работать вне рабочей папки")
        else:
            os.rmdir(name)


def file_work():
    print("Чтобы работать с файлом, введите имя файла с расширением (если хотите работать в другой папке вводите оносительный путь), а потом в меню выберите действие:")
    path = os.getcwd()+"/"+dirname+"/"+str(input())
    print(path)
    if dirname not in path:
        print("Нельзя работать вне рабочей папки")
    else:
        print(
            "Чтобы создать файл нажмите 1" + "\n" + "Чтобы Удалить файл нажмите 2" + "\n" + "Чтобы вывести данные из файла на экран нажмите 3" + "\n" + "Чтобы записать в файл строку нажмите 4" + "\n" + "Чтобы переименовать файл нажмите 5" + "\n" + "Чтобы скопировать файл нажмите 6" +"\n"+"Чтобы переместить файл нажмите 7")
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
            print("Введите новое название")
            text1 = os.getcwd()+"/"+dirname+"/"+str(input())
            os.rename(path, text1)
        elif choice == 6:
            print("Введите новый относительный путь (от корневой папки) с названем файла и расширением")
            print(path,os.getcwd())
            text2 =os.getcwd() +"/"+dirname+str(input())
            shutil.copyfile(path, text2)
        elif choice == 7:
            print("Введите куда переместить файл (относительный путь (от корневой папки) с названем файла и расширением)")
            print(path,os.getcwd())
            text2 =os.getcwd() +"/"+dirname+str(input())
            os.replace(path, text2)


while True:
    os.chdir(tecdir)
    print("Вы находитесь в программе 'простейший файловый менеджер' для работы  умолчанию была создана директория 'forUnix'" + '\n'
        "Для создания или удаления директории нажмите 1" + '\n' + "Нажмите 2 для вызова командной строки и работы вручную" + '\n' + "Для всей работы с файлами нажмите 3" + '\n' + "Чтобы переименовать рабочую директорию введите 4" + '\n' + "Для выхода нажмите 5")
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
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
    elif inp == 4:
        print("Введите имя новой директории")
        dirname = input()
        os.chdir(dirname)
    elif inp == 5:
        sys.exit()