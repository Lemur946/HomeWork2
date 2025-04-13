import json
from typing import Any, Union

from src.main import Category
from src.utils import product_from_json, read_json


def test_read_json(tmp_path: Union[Any | Any]) -> None:
    """
    Test a function that reads a JSON file and returns its contents as a dictionary.
    """

    test_data = [{"key": "value"}]
    file_path = tmp_path / "test.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f)

    result = read_json(str(file_path))

    assert result == test_data


def test_product_from_json() -> None:
    """
    Test of function converting data from JSON to list of objects
    """

    mock_data = [
        {
            "name": "Electronics",
            "description": "Gadgets",
            "products": [
                {"name": "Laptop", "description": "High-end", "price": 1500.0, "quantity": 10},
                {"name": "Phone", "description": "Smartphone", "price": 800.0, "quantity": 15},
            ],
        }
    ]

    categories = product_from_json(mock_data)

    assert len(categories) == 2

    # First category check
    cat1 = categories[0]
    assert isinstance(cat1, Category)
    assert cat1.name == "Electronics"
    assert cat1.description == "Gadgets"
    assert len(cat1.products) == 2
    assert cat1.products[0].name == "Laptop"

    # Second category check
    cat2 = categories[1]
    assert len(cat2.products) == 2
    assert cat2.products[0].name == "Laptop"
    assert cat2.products[1].name == "Phone"
