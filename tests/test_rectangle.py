
def test_area(some_rectangle):
    assert some_rectangle.area() == 10 * 20


def test_perimeter(some_rectangle):
    assert some_rectangle.perimeter() == 10 * 2 + 20 * 2


def test_not_equal(some_rectangle, another_rectangle):
    assert some_rectangle != another_rectangle
