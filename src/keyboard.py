class LanguageMixin:
    def __init__(self):
        self.language = 'EN'

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self


class Keyboard(LanguageMixin):
    all = []

    def __init__(self, name, price, quantity):
        super().__init__()
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __str__(self):
        return f'{self.name}'
