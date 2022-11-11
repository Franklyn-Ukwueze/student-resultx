import pytest
from fuel import convert, fuel_lvl


def test_convert():
    assert convert("0/1") == 0
    assert convert("1/2") == 50
    assert convert("4/4") == 100


def test_value_error():
    with pytest.raises(ValueError):
        convert("x/y")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert fuel_lvl(0) == "E"
    assert fuel_lvl(1) == "E"
    assert fuel_lvl(2) == "2%"
    assert fuel_lvl(98) == "98%"
    assert fuel_lvl(99) == "F"
    assert fuel_lvl(100) == "F" 