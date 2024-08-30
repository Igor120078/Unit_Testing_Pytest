import pytest
import time
import source.some_functions as some_functions


def test_add_numbers():
    result = some_functions.add(1, 4)
    assert result == 5


def test_add_strings():
    result = some_functions.add('First', 'Name')
    assert result == 'FirstName'


def test_divide():
    result = some_functions.divide(15, 3)
    assert result == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        some_functions.divide(10, 0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = some_functions.add(1, 4)
    assert result == 5


@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert some_functions.add(1, 2) == 3


@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    some_functions.divide(3, 0)

