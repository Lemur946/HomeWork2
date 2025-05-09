import pytest

from src.main import BaseProduct, Category, LawnGrass, PrintMixin, Product, Smartphone


class TestBaseProduct:
    """
    Class for test an abstract base class for products that defines required methods.
    """

    def test_abstract_class(self) -> None:
        """
        test an abstract base class for products that defines required methods.
        """
        with pytest.raises(TypeError):
            BaseProduct()


class TestPrintMixin:
    """
    Class for test mixin for adding functionality to display product information.
    """

    def test_mixin_repr(self, capsys: None) -> None:
        """
        test mixin for adding functionality to display product information.
        """

        class TestClass(PrintMixin):
            def __init__(self) -> None:
                self.name = "Test"
                self.description = "Test desc"
                self._PrintMixin__price = 100.0
                self.quantity = 5
                super().__init__()

        obj = TestClass()
        captured = capsys.readouterr()
        assert captured.out.strip() == repr(obj)

    def test_mixin_property(self) -> None:
        """test mixin for adding functionality to display product information."""

        class TestClass(PrintMixin):
            def __init__(self) -> None:
                self.name = "Test"
                self.description = "Test desc"
                self.quantity = 1
                self._PrintMixin__price = 150.0

            PrintMixin.__init__(self)

        obj = TestClass()
        assert obj.price == 150.0


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


def test_product_add_error(product_1: Smartphone) -> None:
    """Test of the Error addition method in the category class"""
    with pytest.raises(TypeError):
        assert product_1 + 1


def test_category_str(first_category: Category) -> None:
    """Test method that returns a string in the category class"""
    assert str(first_category) == "Смартфоны, количество продуктов: 27 шт."


def test_add_product_valid(sample_category: Category, new_product: Product) -> None:
    initial_count = Category.product_count
    sample_category.add_product(new_product)
    assert len(sample_category.products.split("\n")) == 3
    assert Category.product_count == initial_count + 1


def test_add_product_invalid(sample_category: Category) -> None:
    with pytest.raises(TypeError):
        sample_category.add_product("invalid product")


def test_smartphone_init(smartphone_1: Smartphone) -> None:
    """Tests the correct initialization of the Smartphone object."""
    assert smartphone_1.name == "Iphone 15"
    assert smartphone_1.description == "512GB, Gray space"
    assert smartphone_1.price == 210000.0
    assert smartphone_1.quantity == 8
    assert smartphone_1.efficiency == 98.2
    assert smartphone_1.color == "Gray space"
    assert smartphone_1.memory == 512
    assert smartphone_1.model == "15"


def test_smartphone_add(smartphone_1: Smartphone, smartphone_2: Smartphone) -> None:
    """Test of the magical addition method in the category class"""
    assert smartphone_1 + smartphone_2 == 2580000.0


def test_smartphone_add_error(smartphone_1: Smartphone) -> None:
    """Test of the Error addition method in the category class"""
    with pytest.raises(TypeError):
        assert smartphone_1 + 1


def test_lawn_grass_init(lawn_grass_1: LawnGrass) -> None:
    """Tests the correct initialization of the LawnGrass object."""
    assert lawn_grass_1.name == "Газонная трава"
    assert lawn_grass_1.price == 500.0
    assert lawn_grass_1.quantity == 20
    assert lawn_grass_1.description == "Элитная трава для газона"
    assert lawn_grass_1.color == "Зеленый"
    assert lawn_grass_1.country == "Россия"
    assert lawn_grass_1.germination_period == "7 дней"


def test_lawn_grass_add(lawn_grass_1: Smartphone, lawn_grass_2: Smartphone) -> None:
    """Test of the magical addition method in the category class"""
    assert lawn_grass_1 + lawn_grass_2 == 16750.0


def test_lawn_grass_add_error(lawn_grass_1: Smartphone) -> None:
    """Test of the Error addition method in the category class"""
    with pytest.raises(TypeError):
        assert lawn_grass_1 + 1


def test_middle_price(first_category):
    assert first_category.middle_price() == 140333.33333333334
