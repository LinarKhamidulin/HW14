import pytest

from src.classes import Product, Category, Smartphone, LawnGrass


@pytest.fixture
def product_1():
    product_1 = Product('prod_1', "1", 2, 10)
    return product_1


@pytest.fixture
def product_2():
    product_2 = Product('prod_2', "1", 3, 1)
    return product_2


def test_add_product(product_1, product_2):

    assert product_1 + product_2 == 23


@pytest.fixture
def product_3():
    product_3 = Smartphone('prod_1', "1", 2, 10, 2.3, "model",  1, "color")
    return product_3


@pytest.fixture
def product_4():
    product_4 = LawnGrass('prod_2', "1", 3, 1, "country", "germination_period", "color")
    return product_4


def test_add_product_error(product_3, product_4):
    with pytest.raises(TypeError):
        product_3 + product_4