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


book_list_view(library)
print()

add_book("Полтава", "Пушкин А.С.", "2020")

book_list_view(library)
