from src.main import Category, Product


def test_main_product_init(product: Product) -> None:
    """
    Tests the correct initialization of the Product object.
    """
    assert product.name == "Телевизоры"
    assert product.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром," " станет вашим другом и помощником"
    )
    assert product.price == 145222.5
    assert product.quantity == 5
    # Price Setter Test
    product.price = -100
    assert product.price == 145222.5  # The price should not change
    product.price = 200000
    assert product.price == 200000


def test_main_category_init(first_category: Category, second_category: Category) -> None:
    """
    Tests the correct initialization of Category objects.
    """
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получение дополнительных функций для удобства жизни"
    )
    assert first_category.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
    assert second_category.name == "Телевизоры"
    assert second_category.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром," " станет вашим другом и помощником"
    )
    assert second_category.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'
    assert Category.category_count == 2
    assert Category.product_count == 4


def test_product_str(product: Product) -> None:
    """Test method that returns a string in the product class"""
    assert str(product) == "Телевизоры, 145222.5 руб. Остаток: 5 шт."


def test_product_add(product_1: Product, product_2: Product) -> None:
    """Test of the magical addition method in the category class"""
    assert product_1 + product_2 == 1300.0


def test_category_str(first_category: Category) -> None:
    """Test method that returns a string in the category class"""
    assert str(first_category) == "Смартфоны, количество продуктов: 3 шт."
