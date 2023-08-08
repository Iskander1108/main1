# 28.07.23
 
# my_str = "Привет Андрей"
# print(my_str.lower(), "| > lower") # Переводит все в нижний регистр
# print(my_str.upper(), "| > upper") # Переводит все в верхний регистр
# print(my_str.title(), "| > title") # ПЕреводит каждое слово первую букву в верхний регистр
# print(my_str.capitalize(), "| > capitalize") # Переводит первую букву верхний регистр остальные все слова с маленькой буквы
# print(my_str.swapcase(), "| > swapcase") # Все маленькие буквы делает большие а все беольшие в маленькие

# string = input("Напиши свое Имя: ")# input это функция которая принимает типы string(str)
# if string.upper() == "ПРИВЕТ":
#     print("Привет")
# else:
#     print("А мы знакомы!")


# str2 = input("Напиши что-то ")
# print(str2.isdigit(), "| > isdigit") # Все ли состоит из цифр
# print(str2.isalpha(), "| > isalpha") #Все ли состоит только из букв
# print(str2.isidentifier(), "| > isidentifier")# все ли пишется слитно
# print(str2.islower(), "| > islower") # все ли состоит из нижнего регистра
# print(str2.isupper(), "| > isupper") # все ли состоит из верхнего регистра
# print(str2.isnumeric(), "| > isnumeric") # все ли состоит из цифр (пришел со старого пайтона)
# print(str2.istitle(),"| > istitle") # все ли слова в верхнем регистре только первая буква в слове
# print(str2.isspace(), "| > isspace")# все ли состоит  только из пробелов
# print(str2.isprintable(),"| > isprintable")# 
# print(str2.isalnum(),"| > isalnum")#  все ли состоит только из букво-цифреных символов без пробелов и спецсимволов


# text = "   Привет Андрей   "

# print(text.strip(), "| > strip")# Удаляет пробела слева и справа, в центре не удаляет
# print(text.lstrip(), "| > lstrip")# Удаляет пробелы слева
# print(text.rstrip(), "| > rstrip")# Удаляет пробелы справа


# print(text.split(), "| > split") # разделяет и оборачивает в list
# print(text.partition("П"))#раазделяет и оборачивает в tuple(обязательно нужно указывать что разедять)


# text = "Привет Андрей"
# a = f"""            
# input: hello
# output: {text}
# """                           #форматирование строк(f-строка. format). обязательно нужно ставить{}
# print(a)


# text = "Привет Андрей"
# a ="""            
# input: hello
# output: {0} {1} {2} {3}
# """                           #Заполнение текста с помощью индексов {0} {1} {2} {3}  ит.д для заполнения используем formar и внутри format указываем чем заменить индекс
# print(a.format(text, "world", [1,2,3], True))


# h = "hello 123"

# # print(h.replace("123", "*")) # метод замены принимает что заменить и на что заменить
# print(h.startswith("hello"))# начинается ли текст с указанного слова
# print(h.endswith("123"))# заканчивается ли текст с указанного слова
# print("*".join(h))# после каждого символа вставить указанное значение (сначала указываем что вставить потом .join потом куда вставить)


# f = "GGG"

# print(f.center(4, "*")) # Дополнить текст до указанного (4) индексов слева и справо
# print(f.rjust(15, "*"))# Дополнить текст до указанного (15) индексов с слева
# print(f.ljust(15, "*"))#Дополнить текст до указанного (15) индексов с справо
# print(f.zfill(10)) # Дополняет нулями слева до указанного индекса(10)


g = "Привет Андрей"
# #STAR:STOP:STEP
# print(g[:5])
# print(g[::2])
# print(g[0])#вытаскивает первую букву
# print(g[::-1])#переварачивает текст

# print(g.find())
# print(g.index('П'))
# print(g.count("Привет"))

# str = "fgjhkl"
# int = 1
# float = 2.1
# bool = True
# None = пустое значение

# Массивы
# tuple = ()
# list = []
# set = {}
# frozenset({})
# dict = {"key": "value"}

# Условие if elif else  | or, & and, not, is, in


# g = ("gh",123)
# print(g)
# print(g[1])

#изменяемые
# list списки
# set множества
# dict словари


#Неизменяемые
# str строки
# tuple кортежи
# frozenset Неизменяемые множества
# int, float числа 


