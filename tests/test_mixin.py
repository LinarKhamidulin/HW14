import pytest
from src.classes import Product


def test_mixin(capsys):
    Product('a', 'b',  1, 2)
    captured = capsys.readouterr()
    assert "Product: a, b, 1, 2\n" in captured.out
