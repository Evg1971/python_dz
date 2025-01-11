import time


def time_of_function(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)  # Сохраняем результат выполнения функции
        t2 = time.time()
        print(f"Время выполнения операции составило {t2 - t1} секунд")
        return result  # Возвращаем результат выполнения функции
    return wrapper


@time_of_function
def func_one():
    my_list = [i**2 for i in range(100000000) if i % 2 == 0]
    return my_list  # Возвращаем результат, если это необходимо


@time_of_function
def func_two():
    my_list2 = [i for i in range(100000000) if i % 2 == 1]
    return my_list2  # Возвращаем результат, если это необходимо

# Пример вызова функций


func_one()
func_two()
