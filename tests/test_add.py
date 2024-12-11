import pytest

from src.classes import Product


@pytest.fixture
def product_1():
    product_1 = Product('prod_1', "1", 2, 10)
    return product_1


@pytest.fixture
def product_2():
    product_2 = Product('prod_2', "1", 3, 1)
    return product_2


def test_add_product(product_1, product_2):
    assert product_1 + product_2 == (5, 11)