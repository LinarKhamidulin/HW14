import pytest

from src.classes import Product, Category


@pytest.fixture
def product_1():
    product_1 = Product('prod_1', "1", 2, 10)
    return product_1


@pytest.fixture
def category_1():
    category_1 = Category('cat', 'description', [])
    return category_1


@pytest.fixture
def category_2(product_1):
    category_2 = Category('cat', 'description', [product_1])
    return category_2


def test_str_category(category_1):
    assert str(category_1) == "Категория cat, количество продуктов: 0 шт."


def test_str_category_2(category_2):
    assert str(category_2) == "Категория cat, количество продуктов: 1 шт."


def test_str_product(product_1):
    assert str(product_1) == "prod_1, 2 руб. Остаток: 10 шт."
