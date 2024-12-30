import pytest

from src.classes import Smartphone


@pytest.fixture
def product_1():
    product_1 = Smartphone('prod_1', "1", 2, 10, 2.3, "model",  1, "color")
    return product_1

def test_smartphone(product_1):
    assert product_1.name =='prod_1'
    assert product_1.description == "1"
    assert product_1.price == 2
    assert product_1.quantity == 10
    assert product_1.efficiency == 2.3
    assert product_1.model == "model"
    assert product_1.memory == 1
    assert product_1.color == "color"


