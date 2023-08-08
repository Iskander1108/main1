# 27.07.23
# {} - set
# a = {3,2,1} #Сортирует все что находится внутри него
# print(a)

# a = {1, 2, 3}
# b = {4, 5, 6, 7, 3}
# print(a.isdisjoint(b))   # проверяет пересикаются ли символы , если пересекаются  false  если не пересекается true
# print(a.union(b))        #  Обьединяет set
# print(a.intersection(b)) #   проверяет что повторяется
# print(a.difference(b))   # Показывает каких не хватает символов в указанной переменной(разность)
# print(b - a)
# print(a.symmetric_difference(b)) # симмитричная разность которая возвращает недостатки обоих сторон

# a = [1,2,3]
# b = a.copy()
# b.append(4)
# print(a)
# print(b) 

# my_set = {1,}
# my_set.add(2) # добавляет принимает только один обьект 
# my_set.add(False) 
# my_set.add('my text') 
# # print(my_set)
# my_set.remove(1)# удаляет по названию
# my_set.pop()# удаляет первый элемент(по индексу)
# my_set.clear()# 
# print(my_set)

  
# baza_product_name = ["apple", "Banane", "Mango", "Frukt"]
# baza_key_admin = []

# table = input(""" 
# Товары: 1
# Удалить товар: 2
# Добавить товар: 3
# Админка: 4
# Выход: 5
# """)
# if table == '1':
#     print("Все товары", baza_product_name)
# elif table == '2':
#     name = input("Все название товара: ")
#     baza_product_name.remove(name)
#     print(baza_product_name)
# elif table == '3':
#     name = input("Все название товара: ")
#     baza_product_name.append(name)
#     print(baza_product_name)
# elif table == '4':
#     print("Функция пока не доступна")
# elif table == '5':
#     pass
# else:
#     print("Такой команды нет")


#Задание 0

# text = [(1),(2),(3),(4),(5)]
# print(text)

#Задание 1

# text = (1, 2, 3)
# print(text[2])

#Задание 2

# text = ['str', 123, 1,2, True, ('num')]
# print(text)

#Задание 3

# text = ['one', 'mango', 'banana', 'very', 'well'] 
# empty = ' '.join(text)
# print(empty)

#Задание 4

# a = ["hello"]
# b = ["world"]
# a.extend(b)
# print(a)

#Задание 5

# a = ['jack','jack','jack','jon','john']
# print(a.count('jack'))

#Задание 6

# a = ['Oskar', 'Omar', 'Askar']
# a.remove('Oskar')
# print(a)

#Задание 7
# text = []
# a = input('Введите имя: ')
# b = input('Введите возраст: ')
# c = input('Введите любимый язык программирования : ')
# text.append(a)
# text.append(b)
# text.append(c)

# print(text)

#Задание 8

# text = ['name','loop', 'Oskar', '123']
# p = text.index('loop')
# text.pop(p)
# print(text)

#Задание 9

# text = [3, 5, 6, 7]
# print(sum(text)* len(text))


#Задание 10

a = 'hello world 1234'
b = a.isdigit()
numbers = []
letters = []





