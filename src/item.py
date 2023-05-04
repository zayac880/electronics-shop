import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        try:
            assert len(value) <= 10
            self._name = value
        except AssertionError:
            pass

    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('C:/Users/Alex/Desktop/OOP/electronics-shop/src/items.csv') as f:
            reader = csv.DictReader(f)
            items = []
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
                items.append(item)
            cls.all.clear()
            cls.all.extend(list(items))

    @staticmethod
    def string_to_number(value: str):
        try:
            return int(value)
        except ValueError:
            return int(float(value))
