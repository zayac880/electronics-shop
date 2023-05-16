from src.item import Item


class Phone(Item):
    all = []

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        self.all.append(self)

    def __repr__ (self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'


