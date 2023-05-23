class LanguageMixin:
    def __init__(self):
        self.language = 'EN'

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value not in ["RU", "EN"]:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        self._language = value


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
