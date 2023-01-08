def test_something():
    assert 1==2, "мы проверяем это просто для теста, оно должно падать"


def test_one():
    assert_digit(4,5)

def assert_digit(one,two):
    assert one > two, "второе число не меньше первого"