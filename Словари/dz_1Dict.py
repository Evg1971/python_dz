team = [
    {'name': 'Petr', 'grades': [85, 90, 99]},
    {'name': 'Olga', 'grades': [80, 88, 82]},
    {'name': 'Vika', 'grades': [74, 80, 80]},
    {'name': 'Vadim', 'grades': [62, 68, 75]}
]


def calculate_average(grades):
    try:
        return sum(grades) / len(grades)
    except ValueError:
        print('Ошибка. Список оценок пуст')
        return 0
    except TypeError:
        print('Ошибка. Введите корректные данные в списке оценок')
        return 0


def student_info(team):
    for student in team:
        average = calculate_average(student['grades'])
        status = 'Успешен' if average >= 75 else 'Отстающий'
        print(f"Студент: {student['name']}")
        print(f"Средний балл: {average:.2f}")
        print(f"Статус: {status}")
        print()

    total_average = sum(calculate_average(student['grades']) for student in team) / len(team)
    print(f"Общий средний балл: {total_average:.2f}")
    print()


print('Список группы:')
student_info(team)

team.append({'name': 'Ivan', 'grades': [98, 96, 100]})
print(f"Добавился новый студент: {team[-1]['name']}")
student_info(team)

student_min_average = min(team, key=lambda student: calculate_average(student['grades']))
team.remove(student_min_average)

print('Окончательная информация: ')
student_info(team)
