import pytest

from src.classes import Product, Category

@pytest.fixture
def category_3():
    product_1 = Product('prod_1', "1", 12, 10)
    product_2 = Product('prod_1', "1", 13, 10)
    cat = Category('cat_10', 'description', [product_1, product_2])
    return cat

def test_middle_price(category_3):

    assert category_3.middle_price() == 12.5


@pytest.fixture
def category():
    cat = Category('cat_1', 'description', [])
    return cat

def test_middle_price_not_products(category):

    assert category.middle_price() == 0


@pytest.fixture
def category_1():
    product = Product('prod_1', "1", 0, 10)
    cat = Category('cat_1', 'description', [product])
    return cat

def test_middle_price_error(category_1):
    assert category_1.middle_price() == 0


