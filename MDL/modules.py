# 04.08.23


# import my_code
# print(my_code.name)


# from core.my_code import name, age
# print(name)

# from core.my_code import *


# from core.my_code import  name, age
# print(name)

# import core.my_code 
# print(core.my_code.name)

# from ..core.my_code import name, age
# print(name)




# 07.08.23

# Встроенные модули

# from datetime import datetime

# date = datetime.today()# Возвращает текущую дату и время (со старого пайтона)
# date = datetime.now()# Возвращает текущую дату и время , берет время с компа не с интренета

# print(date)
# print(date.date())
# print(date.time())
# print(date.year)
# print(date.month)
# print(date.day)
# print(date.hour)
# print(date.minute)
# print(date.second)

# from datetime import date

# p = date.today()
# print(date.year)
# print(date.month)
# print(date.day)



# from datetime import time

# time1 = time(13, 24, 57)
# print(time1)
# print(time1.hour)
# print(time1.minute)
# print(time1.second)


# from datetime import datetime, timedelta

# now = datetime.now()
# print(now)

# day5 = now + timedelta(days = 5)
# print(day5)



# from datetime import datetime

# now = datetime.now()
# print(now)

# fdata = now.strftime("%Y.%m.%d %H:%M:%S")  # редактирует формат времени
# print(fdata)

# pdata = datetime.strptime("2023-08-07 19:40","%Y-%m-%d %H:%M")
# print(pdata)



# from time import time, sleep, gmtime, strftime

# time() # анализирует времяс 1970 года

# print("Начало")
# sleep(5)        # Код засыпает на 5 секунд ( принимает только секунды)
# print("End")

# st = gmtime()
# print(st.tm_hour +6)   # Часовой пояс  = +0
# print(st.tm_min)

# ft = strftime("%Y.%m,%d %H:%M", gmtime()) # часовой пояс = +0
# print(ft)



# from random import random, randint, choice,shuffle,sample,choices

# # r = random()

# print(r)

# r = randint(1,10)
# print(r)

# users = ["Zere", "Ruslan","Said","Temirlan","Nur","Ablai","Kainar","Iskander","Bakhyt","Algat"]
# # print(choice(users))
# shuffle(users)
# print(users)
# print(sample(users,))
# print(choices(users, k = 5))


# from calendar import calendar, month, weekday,weekheader
# w = weekday(2023,8,7)
# a = weekheader(3)
# cal = month(2023,8, w=3, l=2)
# # cal_all = calendar(2023) 
# print(a)


# from os import system

# for i in range(1, 5):
    # system("mkdir {i}")
    
    
# import sys
# print(sys.path)
# print(sys.api_version)
# print(sys.builtin_module_names)








# 1 Обработка даты и времени:
# Создайте функцию, которая принимает строку в формате 
# "YYYY-MM-DD" и возвращает день недели, 
# на который приходится эта дата.


# from datetime import datetime
# from calendar import weekday

# a = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
# date = datetime.now()
# index_weekday = weekday(date.year, date.month, date.day)
# print(a[index_weekday])




# 2 Работа с временем:
# Создайте таймер обратного отсчёта. 
# Пользователь вводит количество секунд, 
# и программа отсчитывает это время, 
# выводя оставшееся количество секунд 
# каждую секунду, пока время не истечет.


# from time import sleep
# s = int(input(">>>"))
# while s > 0:
#     print(s)
#     sleep(5) #Указывается секунды задержки
#     s-=1




# 3 Случайные числа и выбор элементов из списка:
# Напишите программу, которая случайным образом выбирает 
# 3 уникальных пользователя из списка users и печатает их имена.


from random import sample,choices
users = ["Almaty","Astana","Barcelona","Rom"]
print(choices(users , k=3))



