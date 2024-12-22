import pytest

from src.classes import LawnGrass


@pytest.fixture
def product_lawn():
    product_lawn = LawnGrass('prod_2', "1", 3, 1, "country", "germination_period", "color")
    return product_lawn


def test_lawngrass_1(product_lawn):
    assert product_lawn.name == 'prod_2'
    assert product_lawn.description == "1"
    assert product_lawn.price == 3
    assert product_lawn.quantity == 1
    assert product_lawn.country == "country"
    assert product_lawn.germination_period == "germination_period"
    assert product_lawn.color == "color"