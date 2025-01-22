import pytest


# Arrange
@pytest.fixture
def first_entry():
    return 'a'


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append('b')
    assert order == ["a", "b"]


# --------------how this example would work if we did it by hand------------------------
"""
def first_entry():
    return "a"


def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]


entry = first_entry()
the_list = order(first_entry=entry)
test_string(order=the_list)
"""
