user_password = "123python"

while True:
    input_password = input("Введите пароль: ")
    if input_password == user_password:
        print("Поздравляю! Вы ввели правильный пароль")
        break
    else:
        print("Пароль неверный. Попробуйте еще раз")
