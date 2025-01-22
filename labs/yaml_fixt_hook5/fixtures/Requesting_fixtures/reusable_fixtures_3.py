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
    # Assert
    assert order == ['a', 'b']


def test_int(order):
    order.append(2)
    assert order == ['a', 2]

# ----------------
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


def test_int(order):
    # Act
    order.append(2)

    # Assert
    assert order == ["a", 2]


entry = first_entry()
the_list = order(first_entry=entry)
test_string(order=the_list)

entry = first_entry()
the_list = order(first_entry=entry)
test_int(order=the_list)"""
