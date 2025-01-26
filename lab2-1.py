BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """Конструктор для инициализации атрибутов книги:
        индентификатора (book_id);
        названия (book_name);
        количества страниц (book_pages).

        :param id_: Индентификатор книги
        :param name: Название книги
        :param pages: Количество страниц книги"""
        self.book_id = id_
        self.book_name = name
        self.book_pages = pages  # TODO написать класс Book

    def __str__(self) -> str:
        return f'Книга "{self.book_name}"'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id_={self.book_id!r}, name={self.book_name!r}, pages={self.book_pages!r})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
