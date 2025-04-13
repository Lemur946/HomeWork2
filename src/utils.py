import json
import os
from typing import Any, Dict, List

from src.main import Category, Product


def read_json(path: str) -> List[Dict[str, Any]]:
    """Reads a JSON file and returns its contents as a dictionary."""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data: List[Dict[str, Any]] = json.load(file)
    return data


def product_from_json(data: list[dict[str, Any]]) -> List[Category]:
    """Converts data from JSON to a list of Category objects with Product"""
    categorys = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
            category["products"] = products
            categorys.append(Category(**category))
    return categorys
