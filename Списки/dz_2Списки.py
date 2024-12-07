def input_numbers(name):
    numbers = []
    print(f"Введите числа для списка {name} (введите 'стоп' для окончания): ")
    Flag = 1
    while Flag:
        user_input = input()
        if user_input.lower() == 'стоп':
            break
        try:
            num = float(user_input)
            numbers.append(num)
        except ValueError:
            print("Введите корректное число или 'стоп' для окончания")
    return numbers

roster1 = input_numbers("1")
roster2 = input_numbers("2")

result_roster = []
max_length = max(len(roster1), len(roster2))

for i in range(max_length):
    value1 = roster1[i] if i < len(roster1) else 0
    value2 = roster2[i] if i < len(roster2) else 0
    result_roster.append(value1 + value2)


print(f"Список № 1: {roster1}")
print(f"Список № 2: {roster2}")
print("Новый список: {}".format(result_roster))