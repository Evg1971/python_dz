num = int(input("Введите целое положительное число: "))
if num <= 0:
    print("Пожалуйста, введите целое положительное число")
else:
    while num >= 0:
        print(num)
        num -= 1