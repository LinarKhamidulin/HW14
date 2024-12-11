import pytest

from src.classes import Product, Category


@pytest.fixture
def category_1():
    cat = Category('cat_1', 'description', [])
    return cat


@pytest.fixture
def category_2():
    cat = Category('cat_1', 'description', [])
    return cat


def test_add_product_error(category_2):

    assert Category.product_count == 0
    assert category_2.products == ""


def test_add_product(category_1):
    category_1.add_product(Product('prod_1', "1", 2, 10))
    category_1.add_product(Product('prod_2', "1", 3, 1))

    assert Category.product_count == 2
    assert category_1.products == 'prod_1, 2 руб. Остаток: 10 шт.\nprod_2, 3 руб. Остаток: 1 шт.'



