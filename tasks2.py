# PROBLEM 1:
# data = 'Пережевывай непоколебимый эпатаж братьев и сестер' 
# Взять строку data и заменить все буквы Е на число 3.

#data = 'Пережевывай непоколебимый эпатаж братьев и сестер'
#print(data.replace('е', '3'))

# PROBLEM 2:
# a = 'паралелепипед' 
# Спросить у пользователя бувкву и поделить строку 'a' по этому бувкву. 

#a = 'паралелепипед'
#b = input('>>>')
#print(a.split(b))


# PROBLEM 3:

# Создать предложение где одна его половина написана в маленьком регистре, а вторая полностью в большом.

#r = 'Пережевывай непоколебимый эпатаж братьев и сестер'
#mid = len(r) //2
#a = r[ :mid].lower()
#b = r[mid: ].upper()
#print(a+b)

# PROBLEM 4:
# Сделать из булева значения True  - строку.

#a = True
#b = str(a)
#print(type(a))
#print(type(b))

# PROBLEM 5:
# a = "Свобода - это фантом, там нету тепла для меня без тебя"  
# Взять строку 'a' из  и посчитать сколько там слов.

#r = len("Свобода - это фантом, там нету тепла для меня без тебя".split()) 
#print(r)


# PROBLEM 4:
# Спросить у пользователя имя, возраст и любимый фильм.
# 1.Поприветствовать по имени.
# 2.Похвалить его фильм. 

#a = input('Введите имя ')
#b = int(input('Введите возраст '))
#c = input('Любимый фмильм ')
#print(f'Тебя зовут {a} \nОтличный фильм {c}')


# PROBLEM 6:
# a = "Google Collab all the time" 
# Возмите предложение 'a' и после каждого символа проставить символ '|' 

#a = "Google Collab all the time"
#print(' | '.join(a.split()))




# PROBLEM 7:
# a = """
# Мы больше не летаем и это не наши сны,
# Этот остров необитаем и в нем нет весны.
# И мы не производим больше искры на свет,
# И как бы есть, но как будто бы нас нет.
# """ 
# Взять строку 'a' и сделать каждое её слово с большой буквы.

a = """
 Мы больше не летаем и это не наши сны,
 Этот остров необитаем и в нем нет весны.
 И мы не производим больше искры на свет,
 И как бы есть, но как будто бы нас нет.
 """ 
print(a.title())





#№ 8
# Запросить у пользователя 2  предложения
# обедините их в обратном порядке
# посчитайте длину слов
# и умножте его на 7 
# и найдите их 5 степень 
# и переконвертируйте его на стринг 
# и выведите на экран второе число

#№ 9
# phone = '8 700 736 9090'
# измените номер так чтобы номер был в международом формате
# и был без пробелов

#№ 10
# запросите у пользовотеля 2 слова
# узнайтие начинаются ли оба на одинаковую букву

# № 11
# зпросите возраст пользователя
# и скажите сколько лет ВАМ
# ВАМ 2 раза больше лет чем когда
# он был на 4 года младше
