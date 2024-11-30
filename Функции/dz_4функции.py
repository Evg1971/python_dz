def max_number(a, b):
    if a >= b:
        return a
    else:
        return b


def empty_function():
    pass


def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


def test_max_number():
    assert max_number(3, -9) == 3, "Ошибка: max_number(3, -9) должно быть равно 3"
    assert max_number(-3, -1) == -1, "Ошибка: max_number(-3, -1) должно быть равно -1"
    assert max_number(5, 5) == 5, "Ошибка: max_number(5, 5) должно быть равно 5"
    assert max_number(0, 0) == 0, "Ошибка: max_number(0, 0) должно быть равно 0"


test_max_number()
print("Все тесты пройдены")
