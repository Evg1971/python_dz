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
        print("Список книг в библиотеке: ")
        for book in library:
            print(book)


book_list_view(library)
