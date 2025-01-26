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
    # TODO написать класс Book


class Library:
    emp_list = []

    def __init__(self, books=None):
        """Конструктор для инициализации атрибута списка книг библиотеки."""
        if books is None:
            self.books_list = []
        else:
            self.books_list = books  # TODO написать класс Library

    def get_next_book_id(self) -> int:
        """Метод, возвращающий идентификатор для добавления новой книги в библиотеку.

        :return: Индентификатор новой книги, который равен индентификатору последней книги библиотеки,
        увеличенный на 1
        """
        if len(self.books_list) != 0:
            return self.books_list[-1].book_id + 1
        return 1

    def get_index_by_book_id(self, search_book_id: int) -> int:
        """Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.

        :param search_book_id: Индентификатор книги, индекс которой необходимо найти
        :raise ValueError: Если книги с запрашиваемым id не существует

        :return: Индекс искомой книги в списке библиотеки
        """
        if self.get_next_book_id() != 1:
            for i, book in enumerate(self.books_list):
                if book.book_id == search_book_id:
                    return i
        else:
            raise ValueError('Книги с запрашиваемым id не существует')


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
