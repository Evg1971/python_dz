user_password = "123python"
is_authenticated = False

while not is_authenticated:
    input_password = input("Введите пароль: ")
    if input_password == user_password:
        print("Поздравляю! Вы ввели правильный пароль")
        is_authenticated = True
    else:
        print("Пароль неверный. Попробуйте еще раз")
