# 1 Создайте список с числами от 1 до 5. Выведите сумму чисел в списке.

# my_list = [1,2,3,4,5]
# total = sum(my_list)
# print("сумма =", total)


# 2 Даны два множества. Найдите и выведите объединение этих множеств.

# set1 = {1,2,3}
# set2 = {'abc'}
# print(set1.union(set2))


# 3 Создайте словарь с названиями фруктов и их количеством. Попросите пользователя ввести название фрукта и выведите количество.

# fruit = { 
#     "apple": "20",
#     "mango": "15",
#     "strawberry": "10"
# }
# name = input("Введите название фрукта ").lower()

# if name in fruit:
#     print(name, ":", fruit[name])
# else:
#     print("Фрукт с таким именем отсутсвует")


# 4 Напишите программу, которая принимает строку и проверяет, начинается ли она с "Привет".

# str = input("ВВедите текст")
# if str.lower().startswith("привет"):
#     print("Строка начинается с Привет")
# else: 
#     print("Строка не начинается с Привет")


# 5 Спросите пользователя его возраст. Если возраст больше 18 лет, выведите "Вы совершеннолетний". В противном случае выведите "Вы несовершеннолетний".

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Совершеннолетний")
# else:
#     print("Несовершеннолетний")


# 6 Напишите программу, которая проверяет, состоит ли данная строка только из цифр.

# a = input("Введите цифры: ")
# print(a.isdigit())


# 7 Создайте функцию, которая принимает строку и преобразует ее в верхний регистр.

# a = input("Введите текст: ")
# print("Результат: ",a.upper())


# 8 Создайте список чисел. Выведите наибольшее и наименьшее числа в списке.

# set = [12,25,63,24,75]
# print("Наибольшее число",max(set))
# print("Наименьшее число",min(set))


# 9 Для данного списка чисел найдите сумму всех четных чисел.

numbers = [1,2,3,4,5,6,7,8,9,10]

print(sum(filter(lambda x: x % 2==0, numbers)))

# count = 0

# for i in numbers:
#     if i % 2 == 0:
#         print("Результат")
#         count += i
#     else:
#         print(i,"no")  
  
# print(count)

# 10 Напишите программу, которая подсчитывает количество вхождений определенного элемента в списке.

# a = input("Введите значение: ")
# b = input("Введите значение для подсчета: ")
# print(a.count(b))


# 11 Создайте функцию, которая принимает два списка и возвращает новый список, содержащий элементы, которые есть в обоих списках.

# list = [1,2,3,4,5,6]
# list2 = [1,3,5,6,7,8]
# a = set(list)
# b = set(list2)
# result = a.intersection(b)
# print(result)      \\\\\\\\\\\\\\\\\\\\\\\\выдает в множестве SET


# 12 Напишите программу, которая удаляет все вхождения определенного элемента из списка.

d =[5, 7, 8, 8, 9, 8]

while 8 in d:
    d.remove(8)


print(d)

# https://operavps.com/docs/install-google-chrome-on-ubuntu/
# 13 Создайте словарь с названиями стран и их столиц. Попросите пользователя ввести название страны и выведите ее столицу.

# a = {
#     "Germany" : "Berlin",
#     "Spain" : "Madrid",
#     "Italy" : "Pome",
#     "France" : "Paris"
# }
# b = input("Введите страну: ").title()

# if b in a:
#     print(b, ":", a[b])
# else:
#     print("Такой страны нет.")

# 14 Спросите у пользователя его возраст. Если возраст меньше 13 лет, выведите "Вы ребенок". Если возраст от 13 до 18 лет включительно, выведите "Вы подросток". В противном случае выведите "Вы взрослый".

# age = int(input("Введите возраст: "))
# if age < 13:
#     print("Вы ребенок")
# elif age <= 18:
#     print("Вы подросток")
# else:
#     print("Вы взрослый")


# 15 Напишите программу, которая проверяет, заканчивается ли данная строка на ".com".

# text = "SDFSF.com"
# print(text.endswith(".com"))


# 16 Создайте список чисел. Выведите все числа, которые делятся на 3.

# List = [1,2,3,4,5,6,7,8,9] \\\\\\\\\\\\\\\\\


# 17 Создайте функцию, которая принимает список строк и возвращает новый список с отсортированными строками в алфавитном порядке.

# my_list = ["banana", "apple", "orange", "grape","mango"]
# my_list.sort()
# print(my_list)                 \\\\\\\\как сделать через input


# 18 Даны два словаря. Объедините их в один словарь.

# dict1 = {
#     "a" : "10",
#     "b" : "20",
# }
# dict2 = {
#     "c" : "20",
#     "d" : "30"
# }

# #Вариант1# a = dict1 | dict2
# #Вариант2# a = {**dict1, **dict2}
# a = dict1.copy()
# a.update(dict2)
# print(a)

# 19 Напишите программу, которая проверяет, является ли данная строка палиндромом (читается одинаково в обоих направлениях).

# text = input("Введите текст: ")
# if text == text[::-1]:
#     print("Является палидромом")
# else:
#     print("Не является палидромом")


# 20 Создайте функцию, которая принимает список чисел и возвращает новый список с уникальными элементами (без повторений).

# text = [1,2,3,4,4,3,2,1,5,6,7,8,9]
# set1 = set(text)
# print(set1)