# text = 'hello woRld'
# print(text.title(), ' > title') #КАждаязаглавная буква в верхнем регистре
# print(text.upper(), '> Upper') #Все буквы в верхнем регистре
# print(text.lower(), '> Lower') #Все буквы в нижнем регистре
# print(text.capitalize(), '> Capitalize')  # Первая буква в верхнем регистре
# print(text.swapcase(), '> swapcase') # ПЕреводит буквы в нижний регистр в верхний а верхний в нижний регистр 
# ------------------------------------------------------------------------------------------------------------

# a1 = 'Hello 123'
# a2 = 'Hello world'
# a3 = '123456'

# print(a1.isdigit(), '> isdigit') # Проверяет все ли состоит из цифр и возвращает bool значение 
# print(a2.isalpha(), '> isalpha') # Проверяет все ли состоит из букв и возвращает bool значение
# print(a3.isidentifier(), '> isidentifier') # Проверяет все ли пишется слитно
# print(a2.islower(), '> islower') # Проверяет все ли в нижнем регистре
# print(a1.isupper(), '> isupper') # Проверяет все ли в верхнем регистре
# print(a1.isnumeric(), '>isnumeric') #Проверяет все ли состоит из цифр(пришел со старого пайтона)
# print(a1.istitle(), '>istitle') #  ПРоверяет каждую первую заглавную букву вверхнем регистре
# print(a2.isspace(), '>isspace') # Все ли состоит из пробелов
# print(a2.isprintable(), '>isprintable') #можем ли мы это спринтовать
# print(a1.isalnum(), '>isalnum') # Все ли у нас состоит из букво-цифровых символов (без спец символов)



# text = '     у меня дома живет кот по имени Рик        '
# print(text.strip(), '>strip') #убирает пробелы в начале и конце
# print(text.lstrip(), '>lstrip')# Убирает пробелы в начале
# print(text.rstrip(), '>rstrip')# Убирает пробелы в конце

# print(text.strip('у меня'), '>strip') # Удаляет любые символы с начала и с конца
# print(text.lstrip(''))

#text = 'Привет'
# print(len(text))

# print(text[0:6:2])

# print(text.center(25, '*'))# добавляет символы по бокам
# print(text.ljust(25, 'q'))#добавляет символы справа
# print(text.rjust(25, 'q'))#добавляет символы слева
#print(text.zfill(25))#дополняет текст нулями слева)

# name = 'Iskander'
# age = '21'
# gender = 'male'
# info = f'''
# Имя: {name}
# Возраст: {age}
# Пол: {gender}
#  '''
# print(info)

# name = 'Iskander'
# age = '21'
# gender = 'male'
# info = '''
# Имя: {0}
# Возраст: {1}
# Пол: {2}
#  '''
# print(info.format(name,age,gender))


# text = 'Привет, RFrr'
# print(text.replace('RFrr', 'Iskander')) # Что заменить и на что заменить 


# text = 'Python 1C Go C# JavaScript Java C++ 1C Asambler Php'
# print(text.find('1C'))#Ищем в строке под строку 1С
# print(text.find('1C', 8))#Ищем в строке под строку 1С с 8го индекса
# print(text.rfind('1C'))#Ищем в строке под строку 1С справо
# print(text.index('1C'))#Определяем индекс в строке под строки 1С
# print(text.rindex('1C'))#Определяем индексв строке под строки 1С с право 
# print(text.count('1C'))# Сколько раз встречается 1С в строке 
# print(text.count('1C', 8))#Сколько раз встречается 1С в строке с 8го индекса

# text = 'Python'
# print('*'.join(text))# Вставить строку в под строку после каждого символа


# text = 'Python 123, 456, Hello'
# print(text.split())#Разделить строку в под строку и обернуть в список
# print(text.startswith('Python'))#начинается ли строка с 'Python'
# print(text.startswith('2', 3, 8))
# print(text.endswith('o'))#Конец строки с 'o'
