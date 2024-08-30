import pytest
import json
from unittest.mock import Mock
from shoppingCart.shopping_cart import ShoppingCart
from source.item_database import ItemDatabase

@pytest.fixture
def cart():
    return ShoppingCart(10)


def test_can_add_item_to_cart(cart):
    cart.add("apple")
    assert cart.get_size() == 1
    assert cart.get_items() == ["apple"]

def test_added_item_is_in_cart(cart):
    item = "Banana"
    cart.add(item)
    assert item in cart.get_items()

def test_max_cart_size():
    cart = ShoppingCart(10)
    for _ in range(10):
        cart.add("someItem")
    with pytest.raises(OverflowError):
        cart.add("Banana")

def test_can_get_total_price():
    cart = ShoppingCart(5)
    cart.add("apple")
    cart.add("banana")
    with open('shoppingCart/price_map.json') as f:
        prices = f.read()
    price_map = json.loads(prices)
    total_price = cart.get_total_price(price_map)
    assert total_price == 68.8

def test_can_get_total_price_from_db(cart):
    cart.add("apple")
    cart.add("banana")
    cart.add("orange")
    item_database = ItemDatabase()
    item_database.get = Mock(return_value=6.3)
    total_price = cart.get_total_price(item_database)
    assert total_price == 18.9

def test_can_get_total_price_from_db_side_effect(cart):
    cart.add("apple")
    cart.add("banana")
    item_database = ItemDatabase()

    def mock_get_item(item: str):
        if item == "apple":
            return 39.9
        if item == "banana":
            return 28.9
        return 0
    
    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 68.8

