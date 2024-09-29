import os
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, 'w') as file:
                    pass
            with open(self.__file_name, 'r') as file:
                return file.read()
        with open(self.__file_name, 'r') as file:
            return file.read()

    def add(self, *products):
        existing_products = self.get_products().split('\n')
        for product in products:
            if str(product) not in existing_products:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')

# Testing the classes
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())