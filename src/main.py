from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    An abstract base class for products that defines required methods.
    """

    @abstractmethod
    def __init__(self) -> None:
        """Abstract method for initializing the product."""
        pass

    @abstractmethod
    def __add__(self, other: "Product") -> float:
        """Abstract method for adding products."""
        pass


class PrintMixin:
    """
    Mixin for adding functionality to display product information.
    """

    def __init__(self) -> None:
        """Initializes a mixin and prints information about the created object."""
        print(repr(self))

    @property
    def price(self) -> float:
        """Getter for getting the price of a product."""
        return self.__price

    def __repr__(self) -> str:
        """Returns a string representation of the object."""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(PrintMixin, BaseProduct):
    """Product class"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Initializes the product class."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """Returns a string containing product information for the user."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Adds up the total cost of products in the warehouse."""
        if type(other) is Product:
            summ: float = self.price * self.quantity + other.price * other.quantity
            return summ
        raise TypeError

    @property
    def price(self) -> float:
        """Getter for getting the price of a product."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Setter for setting a new price for a product with verification."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Creates a new product instance from the data dictionary."""
        return Product(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )


class Category:
    """Category class"""

    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Initializes the category class"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Returns a string containing information about the category."""
        total_products = 0
        for product in self.__products:
            total_products += product.quantity
        return f"{self.name}, количество продуктов: {total_products} шт."

    @property
    def products(self) -> str:
        """Getter for retrieving formatted information about products."""
        return "\n".join(f"{str(product)}" for product in self.__products)

    def add_product(self, product: Product) -> None:
        """Adds a product to a category and updates counters."""
        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)
        Category.product_count += 1


class Smartphone(Product):
    """A class representing a smartphone."""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str,
    ):
        """Initializes the smartphone class."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Product") -> None:
        """Adds up the total value of smartphones in stock."""
        if type(other) is Smartphone:
            summ: float = self.price * self.quantity + other.price * other.quantity
            return summ
        raise TypeError


class LawnGrass(Product):
    """A class representing lawn grass."""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: str,
            color: str,
    ):
        """Initializes the lawn grass class."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "Product") -> None:
        """Adds up the total cost of lawn grass in stock."""
        if type(other) is LawnGrass:
            summ: float = self.price * self.quantity + other.price * other.quantity
            return summ
        raise TypeError


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
