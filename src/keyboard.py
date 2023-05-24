from src.item import Item


class LanguageMixin:
    def __init__(self):
        self._language = 'EN'

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value not in ["RU", "EN"]:
            raise ValueError("property 'language' of 'KeyBoard' object has no setter")
        self._language = value


class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._name = name
        self._language = 'EN'


