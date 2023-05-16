from src.item import Item


def test_calculate_total_price():
    item = Item("test item", 10, 2)
    assert item.calculate_total_price() == 20


def test_apply_discount():
    Item.pay_rate = 0.9
    item = Item("test item", 10, 2)
    item.apply_discount()
    assert item.price == 9.0
    assert item.calculate_total_price() == 18


def test_set_name():
    item = Item("test item", 10, 2)
    item.name = "new name"
    assert item.name == "new name"


def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('20.5') == 20


def test_item_repr():
    item = Item("test item", 10.99, 5)
    assert repr(item) == "Item('test item', 10.99, 5)"

def test_item_str():
    item = Item("test item", 10.99, 5)
    assert str(item) == "test item"

def test_item_add():
    item1 = Item("Смартфон", 10000, 20)
    other = 100
    assert item1 + other == None

