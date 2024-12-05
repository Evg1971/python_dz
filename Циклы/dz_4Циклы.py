def summa_numbers():
    total = 0
    for x in range(0, 101, 2):
        total += x
    return total


squares_list = [y ** 2 for y in range(1, 10, 2)]


def count_numbers():
    count = 0
    continue_input = True
    while continue_input:
        try:
            number = float(input("Введите число: "))
            if number < 0:
                continue_input = False
            else:
                count += 1
        except ValueError:
            print("Ошибка! Введено не число")
        finally:
            print(f"Текущее количество введенных чисел:{count}")
    print(f"Количество введенных чисел = {count}")


print(summa_numbers())
print(squares_list)
count_numbers()
