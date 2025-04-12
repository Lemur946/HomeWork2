def test_main_product_init(product):
    assert product.name == "Телевизоры"
    assert product.description == ("Современный телевизор, который позволяет наслаждаться просмотром,"
                                   " станет вашим другом и помощником")
    assert product.price == 145222.5
    assert product.quantity == 5

def test_main_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                    "но и получение дополнительных функций для удобства жизни")
    assert first_category.products == [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ]
    assert second_category.name == "Телевизоры"
    assert second_category.description == ("Современный телевизор, который позволяет наслаждаться просмотром,"
                    " станет вашим другом и помощником")
    assert second_category.products == [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ]
    assert first_category.category_count == 2
    assert first_category.product_count == 4
    assert second_category.category_count == 2
    assert second_category.product_count == 4
