class Product:
    def __init__(self, name, weight, category):
        if isinstance(name, str):
            self.name = name
        if isinstance(weight, float):
            self.weight = weight
        if isinstance(category, str):
            self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products: Product):
        current_products = self.get_products()
        file = open(self.__file_name, 'a')
        for i in products:
            if str(i) in current_products:
                print(f'Продукт {str(i)} уже есть в магазине')
            else:
                file.write(str(i) + '\n')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.1, 'Vegetables')
p2 = Product('Spaghetti', 3.0, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__
print(p1)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
