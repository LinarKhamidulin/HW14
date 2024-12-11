import pytest

from src.classes import Product, Category


@pytest.fixture
def product1():
    product1 = Product("model!", "description", 10, 1)
    return product1


@pytest.fixture
def product2():
    product2 = Product("model1", "description", 20, 2)
    return product2


def test_categories(product1):
    category1 = Category('cat_1', 'description', [product1])
    assert category1.name == 'cat_1'
    assert category1.description == 'description'


def test_categories_count(product1,  product2):
    Category.category_count = 0
    Category.product_count = 0

    category_1 = Category('cat_1', 'description', [product1])

    assert category_1.category_count == 1
    assert category_1.product_count == 1

    category_2 = Category('cat_2', 'description', [product2])

    assert category_2.category_count == 2
    assert category_2.product_count == 2
