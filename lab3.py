import doctest


class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Создание и подготовка к работе объекта "Книга"

        :param name: Название книги
        :param author: Автор книги

        Примеры: >>> book = Book("Чернокнижник", "R.W.")  # инициализация экземпляра класса"""
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    """ Класс бумажной книги. """

    def __init__(self, name: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Бумажная книга"

        :param name: Название бумажной книги
        :param author: Автор бумажной книги
        :param pages: Количество страниц бумажной книги

        Примеры: >>> p_book = PaperBook("Персона", "R.W.", 512)  # инициализация экземпляра класса"""
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError('Количество страниц должно быть целочисленным')
        elif value <= 0:
            raise ValueError('Количество страниц должно быть больше нуля')
        self._pages = value


class AudioBook(Book):
    """ Класс аудиокниги. """

    def __init__(self, name: str, author: str, duration: float):
        """
        Создание и подготовка к работе объекта "Аудиокнига"

        :param name: Название аудиокниги
        :param author: Автор аудиокниги
        :param duration: Продолжительность аудиокниги

        Примеры: >>> a_book = AudioBook("Сущность", "R.W.", 5.43)  # инициализация экземпляра класса"""
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError('Продолжительность аудиокниги должна быть числом с дробной частью')
        elif value <= 0:
            raise ValueError('Продолжительность аудиокниги должна быть больше нуля')
        self._duration = value


if __name__ == "__main__":
    doctest.testmod()  # Проверка работоспособности экземпляров классов с помощью doctest
