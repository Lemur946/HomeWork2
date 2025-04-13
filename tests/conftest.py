import pytest

from src.main import Category, Product


@pytest.fixture()
def product() -> Product:
    """
    Fixture for creating a test object Product.
    """
    return Product(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        price=145222.5,
        quantity=5,
    )


@pytest.fixture()
def first_category() -> Category:
    """
    Fixture for creating a test object Category (Smartphones).
    """
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получение дополнительных функций для удобства жизни",
        products=[
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
            {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
        ],
    )


@pytest.fixture()
def second_category() -> Category:
    """
    Fixture for creating a test object Category (TVs).
    """
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром,"
        " станет вашим другом и помощником",
        products=[{"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
    )
