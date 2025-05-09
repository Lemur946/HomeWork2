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
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
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

    def middle_price(self) -> float:
        """Method of calculating the average price of all goods in a class"""
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0


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
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы "
            "при попытке добавить продукт с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
