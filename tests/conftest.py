import pytest
import source.shapes as shapes


# Fixtures which are defined in "conftest.py" file will be accessible from other files

@pytest.fixture
def some_rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def another_rectangle():
    return shapes.Rectangle(7, 8)
