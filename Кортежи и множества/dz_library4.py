library = {
    "Дубровский": {"author": "Пушкин А.С.", "year": "2015", "available": "в наличии"},
    "Скупой рыцарь": {"author": "Пушкин А.С.", "year": "2021", "available": "выдана"},
    "Хамелеон": {"author": "Чехов А.П.", "year": "2020", "available": "в наличии"},
    "Русалка": {"author": "Лермонтов М.Ю.", "year": "2021", "available": "в наличии"},
    "Левша": {"author": "Лесков Н.С.", "year": "2019", "available": "выдана"}
}


def book_list_view(library):
    if not library:
        print("В библиотеке книг нет")
    else:
        print("Библиотечный каталог: ")
        for book, info in library.items():
            print(f"Название книги: '{book}' - автор:{info['author']}, "
                  f"год издания: {info['year']}, статус: {info['available']}")


def add_book(title, author, year):
    if title in library:
        update = input(f"Книга {title} уже существует в библиотеке. "
                       f"Обновить информацию? да/нет: \n").strip().lower()
        if update == 'да':
            library[title] = {"author": author, "year": year, "available": None}
            print(f"Информация о книге {title} обновлена.\n")
        else:
            print(f"Информация о книге {title} не обновлена.\n")
    else:
        library[title] = {"author": author, "year": year, "available": None}
        print(f"Книга '{title}' добавлена в библиотеку\n")


def remove_book(title):
    try:
        if not title in library:
            print(f"Книга '{title}' в библиотеке не найдена.\n")
        else:
            del library[title]
            print(f"Книга '{title}' из библиотеки удалена.\n")
    except KeyError as e:
        print(f"Ошибка доступа к ключу {e}")
    except Exception as e:
        print(f"Произошла другая ошибка: {e}")


def issue_book(title):
    try:
        if title in library:
            if library[title]["available"] == "в наличии":
                library[title]["available"] = "выдана"
                print(f"Книга '{title}' выдана.\n")
            else:
                print(f"Книга '{title}' уже выдана.\n")
        else:
            print(f"Книга '{title}' в библиотеке не числится.\n")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def return_book(title):
    try:
        if title in library:
            if library[title]["available"] == "выдана":
                library[title]["available"] = "в наличии"
                print(f"Книга '{title}' в наличии.\n")
            else:
                print(f"Книга '{title}' уже в наличии.\n")
        else:
            print(f"Книга '{title}' в библиотеке не числится.\n")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


book_list_view(library)
print()

add_book("Полтава", "Пушкин А.С.", "2020")

issue_book("Дубровский")

return_book("Левша")

book_list_view(library)