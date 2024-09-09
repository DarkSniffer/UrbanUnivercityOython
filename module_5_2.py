class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

print(h3)
print(h4)

print(len(h3))
print(len(h4))

