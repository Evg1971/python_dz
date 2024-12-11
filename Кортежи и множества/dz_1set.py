def input_list(name):
    my_list = []
    print(f"Введите данные для: {name} (введите 'стоп' для окончания)")
    Flag = 1
    while Flag:
        user_input = input()
        if user_input.lower() == 'стоп':
            break
        else:
            my_list.append(user_input)
    my_set = set(my_list)
    print(f"Количество уникальных элементов: {len(my_set)}")
    print(f"Список уникальных элементов: {', '.join(my_set)}")


input_list("Список")