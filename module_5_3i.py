class House:
    houses_history = []

    def __new__(cls, *args):  # создаем новый экземпляр класса
        cls.houses_history.append(args[0])  # в список включаем "имя" объекта
        return super().__new__(cls)  # возвращаем ссылку на класс

    def __del__(self, *args):  # определяем метод del для класса
        print(f'{self.name} снесён, но он останется в истории')  # метод прописывает строку

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        lof = []
        if 1 <= new_floor <= self.number_of_floors:
            lof.append(1)
            print(lof[-1])
            for i in lof:
                if 1 <= i < new_floor:
                    lof.append(i + 1)
                    print(lof[-1])
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    #Добавляем математические методы

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    #Добавляем методы добавления значения

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        return self + value

    def __radd__(self, value):
        return self + value




h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
