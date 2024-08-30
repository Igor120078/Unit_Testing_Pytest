import pytest
import source.shapes as shapes


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (8, 64)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("length, width, expected_perimeter",
                         [(5, 7, 24), (6, 3, 18), (9, 6, 30)])
def test_multiple_rectangle_perimeters(length, width, expected_perimeter):
    assert shapes.Rectangle(length, width).perimeter() == expected_perimeter
