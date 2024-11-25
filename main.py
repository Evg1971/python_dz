try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка: Пожалуйста, вводите только числа")
else:
    message = '''
    Выберете математическую операцию:

    + : Сложение
    - : Вычитание
    / : Деление
    * : Умножение

    Ваш выбор:
    '''
    operation = input(message)
    if operation == "+":
        result = num1 + num2
        print(f"Результат сложения: {result}")
    elif operation == "-":
        result = num1 + num2
        print(f"Результат вычитания: {result}")
    elif operation == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Ошибка. Деление на ноль запрещено!!!")
        else:
            print(f"Результат деления: {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"Результат умножения: {result}")
    else:
        print("Ошибка: Неверная математическая операция")