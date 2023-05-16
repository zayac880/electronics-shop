from src.phone import Phone

def test_phone_repr():
    phone = Phone("test phone", 10.99, 5, 2)
    assert repr(phone) == "Phone('test phone', 10.99, 5, 2)"

def test_phone_str():
    phone = Phone("test phone", 10.99, 5, 2)
    assert str(phone) == "test phone"