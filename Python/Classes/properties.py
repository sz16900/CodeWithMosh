# This is the unpythonic way of validation


class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price canot be negative.")
        self.__price = value


product = Product(90)


# Use Properties instead for a pythonic approach

class Product1:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price canot be negative.")
        self.__price = value


product = Product1(10)
product.price = 99
print(product.price)
