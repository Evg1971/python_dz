try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

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
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
except ZeroDivisionError:
    print("Ошибка. Деление на ноль запрещено!!!")
except ValueError:
    print("Ошибка: Пожалуйста, вводите только числа")
else:
    print(f"Результат операции: {result}")