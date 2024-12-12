from typing import Sequence


class Product:

    def __init__(self,name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, price):
        if price < 1:
            print('Цена равна нулю или меньше')

        elif price > 0 and self.__price < price:
            print('Цена 1')
            self.__price = price

        elif self.__price > price:
            print('Цена 2')
            self.__price = price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):

        sum_product_1 = self.price * self.quantity
        sum_product_2 = other.price * other.quantity
        sum_product = sum_product_1 + sum_product_2
        return sum_product



    @classmethod
    def new_product(cls, dict_product: dict):
        products_list = Category.get_product()
        quantity = 0
        price = 0

        for product in products_list:
            if dict_product['name'] in product.name:
                quantity += dict_product['quantity'] + product.quantity
                price = max(dict_product['price'], product.price)

        name = dict_product['name']
        description = dict_product['description']

        return Product(name, description,  price, quantity)


class Category:

    category_count = 0
    product_count = 0
    __products = []


    def __init__(self, name: str, description: str, products: Sequence[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.__products = products
        Category.category_count += 1
        Category.product_count += len(products)


    def __str__(self):
        product_count = 0
        for i in self.__products:
            product_count += i.quantity
        return f"Категория {self.name}, количество продуктов: {product_count} шт."


    def add_product(self, new_product: Product):
        if isinstance(new_product, Product):
            Category.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError


    @staticmethod
    def get_product():
        return Category.__products


    @property
    def products(self):
        list_products = []

        for product in self.__products:
            list_products.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(list_products)

