import pytest

from src.main import Category, LawnGrass, Product, Smartphone


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
            Product(
                name="Samsung Galaxy C23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=180000.0,
                quantity=5,
            ),
            Product(
                name="Iphone 15",
                description="512GB, Gray space",
                price=210000.0,
                quantity=8,
            ),
            Product(
                name="Xiaomi Redmi Note 11",
                description="1024GB, Синий",
                price=31000.0,
                quantity=14,
            ),
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
        products=[
            Product(
                name='55" QLED 4K',
                description="Фоновая подсветка",
                price=123000.0,
                quantity=7,
            )
        ],
    )


@pytest.fixture()
def product_1() -> Product:
    """Fixture for testing the magic addition method in the category class"""
    return Product(
        name="Телевизоры",
        description="Современный телевизор",
        price=100.0,
        quantity=5,
    )


@pytest.fixture()
def product_2() -> Product:
    """Fixture for testing the magic addition method in the category class"""
    return Product(
        name="Смартфоны",
        description="Современный смартфон",
        price=200.0,
        quantity=4,
    )


@pytest.fixture()
def smartphone_1() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture()
def smartphone_2() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture()
def lawn_grass_1() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture()
def lawn_grass_2() -> LawnGrass:
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def sample_category() -> Category:
    products = [Product("P1", "Desc1", 100, 2), Product("P2", "Desc2", 200, 3)]
    return Category("Electronics", "Tech", products)


@pytest.fixture
def new_product() -> Product:
    return Product("P3", "Desc3", 300, 4)
