import doctest


class Plant:
    """ Класс завода. """

    def __init__(self, p_name: str, p_addr: str, p_size: float):
        """
        Создание и подготовка к работе объекта 'Завод'

            :param p_name: Название завода
            :param p_addr: Расположение, адрес завода
            :param p_size: Площадь завода, м^2

        Примеры: >>> plant = Plant('Завод им. Лихачева', '115280, г. Москва, ул. Автозаводская, д. 23А, корп. 2',
        27500000.0)  # инициализация экземпляра класса
        """
        # Сделаем проверку вводимых значений в конструкторе, дабы наследование метаклассов было корректным
        if not isinstance(p_name, str):
            raise TypeError('Название завода должно быть строковым значением')
        if not isinstance(p_addr, str):
            raise TypeError('Расположение завода должно быть строковым значением')
        if not isinstance(p_size, float):
            raise TypeError('Площадь завода должна быть цислом с дробной частью')
        elif p_size <= 0:
            raise ValueError('Площадь завода должна быть больше нуля')
        self.name = p_name
        self.address = p_addr
        self.size = p_size

    def __str__(self) -> str:
        return f'{self.name}, располагающийся по адресу: {self.address}; с совокупной площадью {self.size} м^2'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(p_name={self.name!r}, p_addr={self.address!r}, p_size={self.size!r})"

    def region_effect(self) -> int:
        """Метод класса, позволяющий определить влияние региона расположения завода"""

        federal_city = ['Севастополь', 'Москва', 'Санкт-Петербург']
        central_regions = ['Белгородская', 'Брянская', 'Владимирская', 'Воронежская', 'Ивановская', 'Калужская',
                           'Костромская', 'Курская', 'Липецкая', 'Московская', 'Орловская', 'Рязанская', 'Смоленская',
                           'Тамбовская', 'Тверская', 'Тульская', 'Ярославская']
        north_west_regions = ['Архангельская', 'Вологодская', 'Калининградская', 'Ленинградская', 'Мурманская',
                              'Новгородская', 'Псковская', 'Карелия', 'Коми', 'Ненецкий']
        south_regions = ['Астраханская', 'Волгоградская', 'Ростовская', 'Адыгея', 'Калмыкия', 'Крым', 'Краснодарский']
        north_caucasian_regions = ['Дагестан', 'Ингушетия', 'Северная Осетия', 'Алания', 'Кабардино-Балкарская',
                                   'Чеченская', 'Карачаево-Черкесская', 'Ставропольский']
        volga_regions = ['Кировская', 'Нижегородская', 'Оренбургская', 'Пензенская', 'Самарская', 'Саратовская',
                         'Ульяновская области', 'Башкортостан', 'Марий Эл', 'Мордовия', 'Татарстан', 'Удмуртия',
                         'Чувашская', 'Пермский']
        ural_regions = ['Тюменская', 'Курганская', 'Челябинская', 'Свердловская', 'Ханты-Мансийский', 'Ямало-Ненецкий']
        siberian_regions = ['Омская', 'Новосибирская', 'Томская', 'Иркутская', 'Кемеровская', 'Красноярский',
                            'Алтайский', 'Алтай', 'Хакасия', 'Тыва']
        far_east_regions = ['Саха', 'Якутия', 'Бурятия',  'Забайкальский', 'Камчатский', 'Приморский', 'Хабаровский',
                            'Чукотский', 'Еврейская', 'Амурская', 'Магаданская', 'Сахалинская']
        all_regions = [federal_city, central_regions, north_west_regions, volga_regions, ural_regions, south_regions,
                       siberian_regions, far_east_regions, north_caucasian_regions]
        for i, regions in enumerate(all_regions):
            for region in regions:
                if region in self.address:
                    return len(all_regions) - i

    def square_effect(self) -> float:
        """Метод класса, позволяющий определить эффективность площади завода"""

        return self.region_effect() * self.size ** 0.25


class MachineBuildingPlant(Plant):
    """ Класс машиностроительного завода. """

    def __init__(self, mbp_name: str, mbp_addr: str, mbp_size: float, mbp_num_emp: int):
        """Создание и подготовка к работе объекта "Машиностроительный завод"

            :param mbp_name: Название машиностроительного завода
            :param mbp_addr: Расположение завода, адрес
            :param mbp_size: Площадь машиностроительного завода, м^2
            :param mbp_num_emp: Количество сотрудников машиностроительного завода, чел.

        Примеры: >>> mbp_plant = MachineBuildingPlant('Мытищинский машиностроительный завод',
        'Московская область, г. Мытищи, улица Фрунзе, ВЛ11', 500000.0, 1475)  # инициализация экземпляра класса"""
        super().__init__(mbp_name, mbp_addr, mbp_size)
        self.num_employees = mbp_num_emp

    def __repr__(self) -> str:
        """Перегружаем данный магический метод для завода конкретной отрасли"""
        return f"{self.__class__.__name__}(mbp_name={self.name!r}, mbp_addr={self.address!r}, " \
               f"mbp_size={self.size!r}, mbp_num_emp={self._num_employees!r})"

    def square_effect(self) -> float:
        """Переопределим эффективность площади для конкретной отрасли с учетом влияния сотрудников"""

        return self.region_effect() * self.size ** 0.25 / self._num_employees

    @property
    def num_employees(self) -> int:
        return self._num_employees

    @num_employees.setter
    def num_employees(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError('Количество сотрудников машиностроительного завода должно быть целым числом')
        elif value <= 0:
            raise ValueError('Количество сотрудников машиностроительного завода должно быть больше нуля')
        self._num_employees = value


class MetaPlant(type):
    """ Метакласс для создания других заводов. """

    def __new__(cls, future_class_name: str, future_class_parents: tuple, future_class_attr: dict):
        """ Данный магический метод возвращает новосозданный объект класса.

            :param future_class_name: Название будушего класса
            :param future_class_parents: Родительский(е) класс(ы)
            :param future_class_attr: Атрибуты и методы будущего класса
        """
        uppercase_attr = {}
        for name, value in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = value
            else:
                uppercase_attr[name] = val
        return super(MetaPlant, cls).__new__(cls, future_class_name, future_class_parents, uppercase_attr)

    def __init__(cls, future_class_name: str, future_class_parents: tuple, future_class_attr: dict):
        """ Конструктор новосозданного класса.

            :param future_class_name: Название будушего класса
            :param future_class_parents: Родительский(е) класс(ы)
            :param future_class_attr: Атрибуты и методы будущего класса
        """
        print('Initialising class', future_class_name)
        super(MetaPlant, cls).__init__(future_class_name, future_class_parents, future_class_attr)


if __name__ == "__main__":
    doctest.testmod()
    industry_dict = {'авто': 'Автомобилестроение', 'впк': 'Военно-промышленный комплекс',
                     'лес': 'Лесная/деревообрабатывающая промышленность', 'ме': 'Металлургия', 'маш': 'Машиностроение',
                     'нпз': 'Нефтеперерабатывающая промышленность', 'стм': 'Производство стройматериалов',
                     'тек': 'Текстильная промышленность', 'эн': 'Энергетика'}
    industry_class_dict = {'авто': 'CarPlant', 'впк': 'MilitaryPlant', 'лес': 'LumberPlant', 'ме': 'MetallurgyPlant',
                           'маш': 'MachineBuildingPlant', 'нпз': 'RefineryPlant', 'стм': 'BuildingMaterialsPlant',
                           'тек': 'TextileFabric', 'эн': 'EnergyPlant'}
    # Выведем все доступные отрасли заводов
    for key, val in industry_dict.items():
        print(f'{key:<4} - {val}')

    flag = True
    # Реализуем цикл с выбором отрасли завода для дальнейшей инициализации нужного объекта
    while flag:
        plant_industry = input('Введите сокращенное название отрасли завода из представленных выше: ').lower().strip()
        if plant_industry not in industry_dict.keys():
            print('Отрасль завода должна быть из представленных выше')
        else:
            flag = False

    users_plant_name = input('Введите название завода: ').strip()
    users_plant_address = input('Введите адрес расположения завода с указанием адмистративного района: ').strip()

    try:
        users_plant_size = float(input('Введите площадь завода (м^2): ').strip())
    except ValueError:
        raise KeyboardInterrupt('Площадь завода должна быть цислом с дробной частью')

    # Создадим объект метакласса в зависимости от выбранной отрасли
    class_industry_name = industry_class_dict[plant_industry]
    users_plant_cls = MetaPlant(class_industry_name, (Plant,), dict())
    print('Класс пользовательского завода готов:')
    print(users_plant_cls)
    users_plant = users_plant_cls(users_plant_name, users_plant_address, users_plant_size)
    print('Экземпляр класса пользовательского завода готов:')
    print(users_plant)
    print(users_plant.region_effect())
