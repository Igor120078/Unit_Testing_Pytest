from pay.order import LineItem,Order

def test_empty_order_total() -> None:
    order = Order()
    assert order.total == 0


def test_order_total_one_item() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test1", price=80))
    order.line_items.append(LineItem(name="Test2", price=70))
    # print(order.line_items)
    assert order.total == 150

def test_order_total_three_items() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test1", price=80, quantity=2))
    order.line_items.append(LineItem(name="Test2", price=70, quantity=3))
    order.line_items.append(LineItem(name="Test3", price=100, quantity=5))
    assert order.total == 870

