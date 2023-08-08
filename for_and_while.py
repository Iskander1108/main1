# 31.07.23

# my_list = list(range(10,20))
# print(my_list)


# for while
#start,stop,step

# for i in range(0,10):
#     print("Hello" , i)


# a = [1,2,3,4,5,6]
# b = []
# h = []
# for i in range(1, 101):
#     print(i, end = " ")
#     if i % 2 == 0:
#         b.append(i)     
#     else:
#         h.append(i)


# print(sum(b))
# print(sum(h))


# \n - Переход строки
# \t - На один tab вперед


# for name in "Marselle":
#     n = input("Введите имя: ")
#     print(n)
#     # print(name, end = " ")

# n = [ i for i in range(1,11) if i % 2 == 0]
# print(n)

# for name in [ 1,2,3]:

# users = {
#     "marselle": 20,
#     "user": 40,

# }

# for k, v in users.items():
#     print(k,v)

# for k in users.keys():
#     print(k)

# for v in users.values(): 
#     print(v)



# a = 10

# while a >= 1 :
#     print("hello", a)
#     a = a - 1


# while True:
#     n = input("Напиши что-то: ")

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i,end=" ")
#     else:
#          continue


# while True:
#     num = int(input("Число "))
#     if num >= 10:
#         print(num)
#     else:
#         break




users = {
    "admin": {
        "name": "admin",
        "password": "123123123",
        "phone_number": "+77470560679",
        "balance": 100,
    }
}

key = None
while True:
    table = input("""
1 Зарегестрироваться
2 Авторизоваться 
3 Перевод баланса 
4 Информация                  
5 Выйти                
>>>  """)
    if table == "1":
        username = input("ПРидумайте пользовательское имя: ")
        name = input("Введите имя: ")
        phone = input("Введите номер тел: ")
        password = input("Придумайте пароль: ")
        password1 = input("Повторите пароль: ")

        while password != password1 or len(password1) <= 8:
            password = input("Придумайте пароль: ")
            password1 = input("Повторите пароль: ")

        users[username] = {
            "name": name,
            "password": password1,
            "phone_numder": phone,
            "balance": 100,

        }
        print(users)

        key = username
        print("Вы уже зарегестрированы")
    elif table == "2":
        if key is None:
            """Авторизация"""
            username = input("Введите пользовательское имя: ")
            password = input("Введите пароль: ")
            if username in users and password == users[username]['password']:
                key = username
                print("Вы вошли в аккаунт", username)
            else:
                key = None
                print("Логин или пароль не верный")
        else:
            print("Вы уже авторизованы")
    elif table == "3":
        if key is not None:
            recipient_login = input("Введите логин получателя: ")
            summa = int(input("Введите сумму: "))
            if summa <= users[key]["balance"]:
                users[key]["balance"] -= summa
                users[recipient_login]["balance"] += summa
                print("Транзакция прошла успешно")
            else:
                print("У вас на балансе не достаточно средств")
        else:
            print("Вы не авторизованы")      

 




#  \\\\\\\\\\ Задания \\\\\\\\\\
# #tasks 1

# for i in range(1, 11):
#     print(i)



#tasks 2

# вариант 1
# num = 0
# for i in range(1 ,11):
#      num += i
#      print(num)

# вариант 2
# print(sum(list(range(1, 11))))



#tasks 3

# for i in range(1, 6):
#     print(i**2)
    


#tasks 4

# for i in "Python":
#     print(i, end=" ")


#tasks 5

# text = "python"
# for i in range(0, len(text), 2):
#     print(text[i])

    
#tasks 6

# a = int(input("Введите число: "))
# b = 0
# for i in range(1, a+1):
#     print(i)
#     b += i
# print(b) 


#tasks 7

# n = int(input("Введите число: "))
# count = True
# for i in range(2, int(n)):
#     if n % i == 0:
#         count = False
#         break
# if count:
#     print("Простое")
     
# else:
#     print("Не простое")



#tasks 8

# n = int(input("Ввдеите число: "))
# faktorial = 1
# for i in range(1 , n+1):
#     if n > 1:
#         faktorial *= i
# print("Факториал числа", f"{n} == {faktorial}")


#tasks 9

# n = int(input("Введите число: "))
# for i in range(1, 11):
#     print(f"{n} * {i} = {n*i}")


#tasks 10
# n = int(input("Число: "))
# a = []
# for i in range(1 , n+1):
#     a.append(i)
# print(sum(a) / n)


# people = int(input("Сколько вас: "))
# alls = []
# for i in range(1, people +1):
#     age = int(input("Возраст: "))
#     alls.append(age)

# print(alls)
# print(sum(alls) / people)


