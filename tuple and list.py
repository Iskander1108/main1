#25.07.23 (массивы)

# () - TUPLE  является не изменяемым

#a = 'Hello'
#b = 1

# c = (1 , 'Hello', 1.1, True, False)

# print(c[1::2]) #считает индексы

# c = ('Hello, 1')
# a, b = c
# print(a)
# print(b) 
# print(c[0])


# a = tuple()
# b = 1, 2, 3, 4
# print(b)

# [] - LIST

# a = [1, 'asd', True, (1,2,3)]

# list = [1, 2, 3]

# list.append(1)  # довобляет элемент в конец списка
# list.append(2)
# list.append(3)
# list.append('fgfgdgfd')   # довобляет элемент в конец списка

# print(list)


# a = [1, 2]
# b = [3, 4]

# a.extend(b)
# a.extend([1, 2, 3, 4]) #расширяет список

# print(a)
# print(b)


# a = [1, 2, 3]
# a.insert(2, 'asd') #добавляет
# # a.insert(2, a[2]+1)
# print(a)


# a = [1,2,3,4,[1,2,3'Hello']]
# # # a.remove('Hello') #удаляет
# # # a.remove(a[4])
# a[4].remove('Hello')

# print(a)

# a = [1, 2, 3]
# b = a.pop(1) #удаляет и сохраняет в переменной

# print(a)
# print(b)


# a = [1, 2, 3]
# a.clear()
# print(a)


# a = [1, 3, 2, 4, True, False]
# a.sort()  #сортирует с 0 
# print(a)

# a.reverse() #сортирует в обратном
# print(a)

# a = [1,2,3,4,True]
# print(sum(a)) # Находитсумму листа   считает символы и спец символы



#is 
#in
#not

# a = [1,2,3,4]
# print('Hello' in a)
# if 1 not in a:          # смотрит если ли в переменной символ в данном случае (1)
#     print('not',a)
# else:
#     print('in', a)

# a = [1,2,3,4]
# # print(a is not None) # для сравнения есть или нет
# if a is not None:
#     print('A не пустое')




#Задание 1
# text = input('Введите текст ')
# if text == text[::-1]:
#     print('Строка является палирдромом')
# else:
#     print('Строка не является палиндромом')
    


#Задание 2
# text = int(input('num'))
# if text > 10:
#     print('Число больше 10')
# elif text == 10:
#     print('ЧИсло == 10')
# else:
#     print('Число меньше 10')


#Задание 3
# a = ['f',1,2]
# if str == type(a[0]):
#     print('Первый элемент строка')
# else: 
#     print('Первый элемент не строка')


#Задание 4
# text = [1,2,3,4]
# if not text:
#     print('пусто')
# else:
#     print(' не пусто')


