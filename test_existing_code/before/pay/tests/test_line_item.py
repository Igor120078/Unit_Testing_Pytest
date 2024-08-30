from pay.order import LineItem

def test_line_item_default() -> None:
    line_item = LineItem("Test", 100)
    assert line_item.total == 100


def test_line_item_total_quantity() -> None:
    line_item = LineItem("Test", 50, 5)
    assert line_item.total == 250





