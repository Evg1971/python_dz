try:
    num1 = float(input("Введите число: "))
    num2 = float(input("Введите число: "))
    result = num1 / num2
except ValueError:
    print("Ошибка: Введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
else:
    print(f"Результат: {result}")
finally:
    print("Результат известен")


