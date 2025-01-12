# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
import math
from typing import Union


class RoboticArm:
    def __init__(self, num_modules: int, height: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Роборука"

        :param num_modules: Количество модулей роборуки, шт
        :param height: Высота роборуки, м

        Примеры: >>> robo_arm = RoboticArm(10, 50)  # инициализация экземпляра класса
        """
        if not isinstance(num_modules, int):
            raise TypeError("Количество модулей роборуки должно быть типа int или float")
        if not num_modules > 0:
            raise ValueError("Количество модулей роборуки должно быть больше нуля")
        self.num_modules = num_modules  # инициализируем количество модулей роборуки

        if not isinstance(height, (int, float)):
            raise TypeError("Высота роборуки должна быть типа int или float")
        if not height > 0.1:
            raise ValueError("Высота роборуки должна быть более 0.1 м")
        self.height = height  # инициализируем высоту роборуки

    def get_operation_radius(self) -> float:
        """
        Вычисление радиуса действия роборуки

        :return: Операционный радиус роборуки

        Примеры: \n >>> robo_arm = RoboticArm(10, 50) \n >>> operation_radius = robo_arm.get_operation_radius()"""
        return self.height * 1.75  # Вычисляем операционный радиус роборуки на основе ее высоты

    def get_operation_speed(self) -> int:
        """
        Вычисление количества операций роборуки в минуту

        Примеры: \n >>> robo_arm = RoboticArm(10, 50) \n >>> operation_speed = robo_arm.get_operation_speed()
        """
        return self.num_modules ** 2  # Вычисляем количество операций роборуки на основе числа модулей


class Conveyer:
    def __init__(self, speed: Union[int, float], width: Union[int, float], length: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Конвейер"

        :param speed: Cкорость ленты конвейера, м/с
        :param width: Ширина конвейера, м
        :param length: Длина конвейера, м

        Примеры: >>> conveyer = Conveyer(2.5, 56.5, 3.2)  # инициализация экземпляра класса"""
        if not isinstance(speed, (int, float)):
            raise TypeError("Cкорость ленты конвейера должна быть типа int или float")
        if speed <= 0:
            raise ValueError("Cкорость ленты конвейера должна быть больше нуля")
        self.speed = speed  # инициализируем скорость ленты конвейера

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина конвейера должна быть типа int или float")
        if width < 0.5:
            raise ValueError("Ширина конвейера должна быть не менее 0.5 м")
        self.width = width  # инициализируем ширину конвейера

        if not isinstance(length, (int, float)):
            raise TypeError("Длина конвейера должна быть типа int или float")
        if length < 2:
            raise ValueError("Длина конвейера должна быть не менее 2 м")
        self.length = length  # инициализируем длину конвейера

    def is_efficiency(self, operation_volume: Union[int, float], out_capacity: Union[int, float]) -> bool:
        """
        Проверка является ли конвеер достаточно производительным для заданных объемов и требуемой производительности

        :param operation_volume: Объем загружаемого сырья, [шт, м^3]
        :param out_capacity: Требуемая выходная производительность конвейера, [шт/с, м^3/с]

        :return: Является ли конвейер производительным

        Примеры: \n >>> conveyer = Conveyer(2.5, 56.5, 3.2) \n >>> conveyer.is_efficiency(5, 22.5)
        """
        if not isinstance(operation_volume, (int, float)):
            raise TypeError("Объем загружаемого сырья должен быть типа int или float")
        if operation_volume <= 0:
            raise ValueError("Объем загружаемого сырья должен быть больше нуля")
        return operation_volume / (self.length / self.speed) >= out_capacity

    def increase_speed(self, delta_speed: Union[int, float]) -> None:
        """
        Увеличение скорости конвейера
        :param delta_speed: Значение увеличения скорости

        :raise ValueError: Если увеличение скорости меньше нуля, то вызываем ошибку

        Примеры: \n >>> conveyer = Conveyer(2.5, 56.5, 3.2) \n >>> conveyer.increase_speed(0.6)
        """
        if not isinstance(delta_speed, (int, float)):
            raise TypeError("Значение, на которое увеличиваем скорость, должно быть типа int или float")
        if delta_speed <= 0:
            raise ValueError("Увеличение скорости должно быть больше нуля")
        self.speed += delta_speed


class MachineBuildingPlant:
    def __init__(self, num_conveyer: int, num_roboarm: int):
        """
        Создание и подготовка к работе объекта "Машиностроительный завод"

            :param num_conveyer: Количество конвейеров завода
            :param num_roboarm: Количество роборук завода

        Примеры: >>> mb_plant = MachineBuildingPlant(5, 3)  # инициализация экземпляра класса"""
        if not isinstance(num_conveyer, int):
            raise TypeError("Количество конвейеров завода должно быть типа int")
        if num_conveyer <= 0:
            raise ValueError("Количество конвейеров завода должно быть больше нуля")
        self.num_conveyer = num_conveyer  # инициализируем количество конвейеров завода

        if not isinstance(num_roboarm, int):
            raise TypeError("Количество роборук завода должно быть типа int")
        if num_roboarm <= 0:
            raise ValueError("Количество роборук завода должно быть больше нуля")
        self.num_roboarm = num_roboarm  # инициализируем количество роборук завода

    def is_enough_roboarm(self) -> bool:
        """
        Функция, которая проверяет достаточно ли на заводе роборук

        :return: Достаточно ли на заводе роборук

        Примеры: \n >>> mb_plant = MachineBuildingPlant(5, 3) \n >>> mb_plant.is_enough_roboarm()
        """
        return self.num_roboarm / self.num_conveyer >= 1.25

    def plant_avg_efficiency(self) -> Union[int, float]:
        """
        Вычисление средней производительности завода

        :return: Среднюю производительность завода

        Примеры: \n >>> mb_plant = MachineBuildingPlant(5, 3) \n >>> plant_efficiency = mb_plant.plant_avg_efficiency()
        """
        return (self.num_roboarm * self.num_conveyer) ** 0.5

    def to_increase_efficiency(self, required_efficiency: Union[int, float]) -> str:
        """
        Вычисление необходимого оборудования для обеспечения требуемой производительности

        :param required_efficiency: Требуемая производительность завода
        :raise ValueError: Если требуемая производительность завода меньше или равна нулю

        :return: Нужно ли дополнительное оборудование и какой объем при необходимости

        Примеры: \n >>> mb_plant = MachineBuildingPlant(5, 3) \n >>> print(mb_plant.to_increase_efficiency(20))"""
        if not isinstance(required_efficiency, (int, float)):
            raise TypeError("Требуемая производительность завода должна быть типа int или float")
        if required_efficiency <= 0:
            raise ValueError("Требуемая производительность завода должна быть больше нуля")
        plant_efficiency = self.plant_avg_efficiency()  # вычислим текущую производительность завода
        if plant_efficiency > required_efficiency:
            return f'Текущая производительность завода превышает требуемую на ' \
                   f'{round((100 * plant_efficiency / required_efficiency), 2)} %'
        elif plant_efficiency == required_efficiency:
            return f'Текущая производительность завода обеспечивает требуемую'
        else:
            extra_conveyer = math.ceil(required_efficiency ** 2 / self.num_roboarm)  # округляем до большего целого
            extra_roboarm = math.ceil(required_efficiency ** 2 / self.num_conveyer)  # округляем до большего целого
            return f'Для обеспечения требуемой производительности дополнительно необходимо: \n ' \
                   f' - {extra_roboarm} роборук(и) \n Или \n - {extra_conveyer} конвейера(ов)'


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
