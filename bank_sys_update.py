from random import choice
baza = {
    "user1" :{
        "phone" : "+77071232323",
        "name" : "Jon",
        "balance" : 9999, 
        "password" : "123qweasd",
        "age" : 24
    }, 
    "user2" :{
        "phone" : "+77776883221",
        "name" : "Nik",
        "balance" : 9350, 
        "password" : "123QWEASD",
        "age" : 43
    }
}

m = None

while True:
    if m is None:
        print(" Добро пожаловать! ")
        a = int(input("""
        1 - Зарегистрироваться
        2 - Авторизоваться
        3 - Перевод баланса
        4 - Список пользователей
        5 - Информация 
        6 - Выйти
        Выберите операцию: """))
    if a == 1:
        login = input("Введите логин: ")
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        age =  int(input("Ваш возраст: "))
        

        def main(size_pass: int, *list1):
            password = []
            for i in range(size_pass):
                password.append(choice(list1))
            return password, 


        size_password = int(input('Размер пароля(Выберети колличество символов в пароле): '))
        end_pass = main(size_password, '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm')
        passs = ''.join(end_pass[0])


        baza.update({
            login: {
                "phone" : phone,
                "name" : name,
                "balance" : 1000,
                "password" : passs
            }
        })
        print(baza)
        print(f"Ваш пароль {passs}")


    elif a == 2:
        if m is None:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in baza.keys() and password == baza[login]["password"]:
                print("Вы авторизованы")
            else:
                print("Неверный логин или пароль")


    elif a ==3:
        if m is not None:
                sum = str(input("Введите сумму: "))
                if sum < baza[login]["balance"]:
                    logbalans = input("Введите логин получателя: ")
                    if logbalans in baza[login]:
                        sum += logbalans["balance"]
                        print(logbalans["balance"])

                    else:
                        print("Такого логина не существует")
                
                else:
                    print("Сумма перевода превышает Ваш текуший баланс")


    elif a == 4:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        if login in baza.keys() and password == baza[login]["password"]:
            print(baza[login]["name"])
        else:
            print("Неверный логин или пароль")


    elif a == 5:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        if login in baza.keys() and password == baza[login]["password"]:
            print(baza.keys())
        else:
            print("Неверный логин или пароль")

    elif a ==6:
        print("До скорой встречи")
        break
    
    else:
        print('убедитесь что вы ввели правильную команду')
