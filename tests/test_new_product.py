import pytest

from src.classes import Product, Category


@pytest.fixture
def category():
    cat = Category('cat_1', 'description', [])
    return cat


def test_new_product(category):
    category.add_product(Product('prod_1', "1", 2, 10))
    category.add_product(Product('prod_2', "1", 3, 1))

    new_product_1 = Product.new_product(
        {"name": "prod_1", "description": "1", "price": 2, "quantity": 10})

    assert new_product_1.name == "prod_1"
    assert new_product_1.description == "1"
    assert new_product_1.price == 2
    assert new_product_1.quantity == 20

    new_product_1.price = 800
    assert new_product_1.price == 800

    new_product_2 = Product.new_product(
        {"name": "prod_2", "description": "1", "price": 3, "quantity": 0})

    assert new_product_2.name == "prod_2"
    assert new_product_2.description == "1"
    assert new_product_2.price == 3
    assert new_product_2.quantity == 1

    new_product_2.price = 800
    assert new_product_2.price == 800


def test_new_product_zero(category):
    category.add_product(Product('prod_2', "1", 3, 1))

    new_product_2 = Product.new_product(
        {"name": "prod_2", "description": "1", "price": 3, "quantity": 0})

    new_product_2.price = 0
    assert new_product_2.price == 3


def test_new_product_minus(category):
    category.add_product(Product('prod_2', "1", 3, 1))

    new_product_2 = Product.new_product(
        {"name": "prod_2", "description": "1", "price": 3, "quantity": 0})

    new_product_2.price = -100
    assert new_product_2.price == 3





