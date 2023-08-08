# 03.08.23

# OPEN()

# Режим  текста
# r      - Только для чтения.
# w      - Только для записи. Создаст новый файл, 
#           если не найдет с указанным именем.

# a      - Откроет для добавления нового содержимого. 
#         Создаст новый файл для записи, если не найдет с указанным именем.

# rb  - Только для чтения (бинарный).
# wb  - Только для записи (бинарный). 
#        Создаст новый файл, если не найдет с указанным именем.


# file = open("text.txt","w") # name file & pars mode
# file.write("Hello world")
# file.close()


# name = input("Напиши имя: ")
# # ParsMode write - "w" Очистить и записать
# file = open("text.txt","w") 
# #write принимает только str
# file.write(name)
# file.close()


#ParsMode Add "a"  Добавить текст
# file = open("text.txt","a") 
# file.write("Hello\n")
# file.close()


#ParsMode Read - "r"  Прочитать текст
# file = open("text.txt","r") 
# src = file.read()
# file.close()

# print(src.count("Hello"))  # если стринг то можно добавлять все методы данных стринг


# with open("text.txt", "r") as file:
#         src = file.read()
# print(src)


with open("text.txt", "r") as h:
    s = h.read()
    # print(len(s.split(" ")))
    
# a = set()
# for i in s:
#       if i.isnumeric():
#            a.add(int(i))
    
# print(sum(a))


# 3. Напишите программу, которая считывает файл и 
# выводит на экран только те строки, 
# которые содержат цифру "2". 
# Для решения задачи нужно использовать for, 
# if и метод строки .find().

# a = []
# for i in s:
#     if i  == "2":
#         a.append(i)
# print(" ".join(a))


# 4. Напишите программу, которая считывает файл и 
# выводит на экран только те строки, 
# которые заканчиваются символом "!" или "?".



# for i in s.split():
#     if i.endswith("!") or i.endswith("?"):
#         print(i)
        



for i in s.split():
    if i.startswith("A") or i.startswith("a"):
        print(i)
