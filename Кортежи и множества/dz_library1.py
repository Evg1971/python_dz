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


book_list_view(library)