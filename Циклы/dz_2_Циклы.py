parol_user = "123python"
parol = input("Введите пароль: ")
while parol != parol_user:
    print("Неверный пароль")
    parol = input("Попробуйте еще раз. Введите пароль: ")
print("Поздравляю! Вы ввели правильный пароль")