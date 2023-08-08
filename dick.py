# 27.07.23

# a = {1,2,3,4}

# a = frozenset([1,3,4]) # тип данных . не изменяемый 
# print(a)

# dict #

# # my_set = {1,}
# my_dict = {
#     'name': 'Iskander',
#     'age': 22,
# }

# print(my_dict['age'])
# print(my_dict['name'])


# users = {
#     'iskander':{
#         'name': 'Iskander',
#         'age': 22,
#         'gender': 'male',
#         'student': {
#             'name': 'ITC',
#             'mentor': 'Marselle',
#             'time': '19:00'

#         }        
#     }
# }

# print(users['iskander']['student']['mentor'])

# my_dick = {
#     'name': 'Iskander',
    
# }

# print(my_dick.items())  #вернуть все ключи и значения в формате list>>>tuple
# print(my_dick.keys())   #вернуть  все ключи в формате list
# print(my_dick.values()) #ввернуть все значения в формате list


# my_dick = {
#     'name':'Iskander',
#     'color':'red',

# }
# test ={
#     'age': 20,
#     'login': {
#         'name1':'Marselle',
#         'name2': 'Kainar',
#     },

# }

#Вариант1. a = dict1 | dict2
#Вариант2. a = {**dict1, **dict2}     #можно обьединять 2 диктери в 1
#Вариант3. a = dict1.copy()
#          a.update(dict2)

# my_dick.update(test['login'])       # расширение диктери, можно создавать dick внутри
# print(my_dick)

# a = {
#     'name': 'marselle',
#     'cart1': [],
#     'cart2': (1,2,3),

# }
# # a['cart1'].append(1)
# a['cart2'] = 123  # Изменить значение ключа cart2 на 123
# a['cart3'] = 'GG' # Создать ключ cart3 c значением GG
# a.update(hh=123)  # Создать ключ hh с значением 123
#a.pop('name')      #Удаляет ключ

# print(a)

#Задание 1

# a = {1,2,3,4,5,6,7,8,9}
# a.remove(7)
# print(a)

#Задание 2

# a = {1,2,3, 'Hello'}
# b = {1,4,5, 'world'}
# print(a.intersection(b))

#Задание 3

# set2 = {1,2,3, 'python'}
# set3 = {2,3, 'c++'}
# print(set3.difference(set2))

#Задание 4

# set = {123,546,'ITC','Almaty','Cake'}
# set.add('008')
# print(set)
# d = set.pop()
# print(d)

#Задание 5, 6

# lunch= {
#     'besh_barmak': '130som',
#     'Lagman': '100som',
#     'borsh': '110som',
# }

# lunch['Lagman']='135som'
# lunch.pop('borsh')
# lunch['drinks']='Caco-cola','Sprite','Fanta'
# print(lunch)

#Задание 7

# set1 = {'add','isdisjoint', 'union', 'intersiction', 'difference','symmetric_difference','remove','clear','pop','copy'}
# set2 = {'clear','copy', 'fromkeys', 'get', 'items','keys','popitem','pop','setdefauld','update','values' }

# print(set1.intersection(set2))