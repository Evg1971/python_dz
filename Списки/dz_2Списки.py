numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]


if len(numbers_1) != len(numbers_2):
    print("Списки должны быть одной длины")
else:
    numbers_summa: list[int] = []
    for i in range(len(numbers_1)):
        numbers_summa.append(numbers_1[i] + numbers_2[i])
print(numbers_summa)
