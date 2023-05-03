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



