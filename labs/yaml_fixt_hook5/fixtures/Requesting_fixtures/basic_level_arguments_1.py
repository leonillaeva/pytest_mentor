# “Requesting” fixtures. At a basic level, test functions request fixtures they require by declaring them as arguments.

import pytest


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit('banana')]


def test_fruit_salad(fruit_bowl):
    """
    test_fruit_salad “requests” fruit_bowl,
    when pytest sees this, it will execute the fruit_bowl fixture function
    and pass the object it returns into test_fruit_salad as the fruit_bowl argument.
    assert all() - checks whether the value 'cubed' equals True for all fruits in the list 'fruit_salad.fruit',
    if not all are True, the test will be failed.
    :param fruit_bowl:
    :return: True, True
    """
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)
    # print(fruit_salad) # -> FruitSalad object at 0x00000193F10A9010

    # for fruit in fruit_salad.fruit:
    #     print(fruit.cubed)
    #     True
    #     True

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)


# Here’s roughly what’s happening if we were to do it by hand:

"""
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)

# ------- Main program -------------
# Arrange
bowl = fruit_bowl()
test_fruit_salad(fruit_bowl=bowl)
"""
