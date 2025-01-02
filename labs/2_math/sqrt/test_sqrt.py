import pytest
from helper import sqrt_1, sqrt_2_with_raises, sqrt_3_with_exceptions

# ---- 1 simple evaluation sqtr ---------------
TEST_SQRT = [
    pytest.param(-25, pytest.raises(ValueError), marks=[pytest.mark.xfail]),
    pytest.param("string", pytest.raises(TypeError), marks=[pytest.mark.xfail]),
    pytest.param("2 3/11", pytest.raises(Exception), marks=[pytest.mark.skip]),
    (0, 0.0),
    (4, 2.0),
    (36, 6.0),
    (36.6, 6.04979338490167),
]


@pytest.mark.parametrize("x, ex_outcome", TEST_SQRT)
def test_sqrt_1(x, ex_outcome):
    result = sqrt_1(x)
    assert result == ex_outcome


# -----2 raises with message---------------------
TEST_SQRT_2_RAISES = [
    (-25, ValueError, "Ошибка! Невозможно найти квадратный корень из отрицательного числа!"),
    ("string", TypeError, "Ошибка! Вы забыли ввести выражение!"),
    (0, None, 0.0),  # None - no exception
    (4, None, 2.0),
    (36, None, 6.0),
    (36.6, None, 6.04979338490167),
]


@pytest.mark.parametrize("x, exception, expected", TEST_SQRT_2_RAISES)
def test_sqrt_2_with_exceptions(x, exception, expected):
    # if expect exception
    if exception:
        with pytest.raises(exception) as except_info:
            sqrt_2_with_raises(x)
        # check exception text
        assert str(except_info.value) == expected
    else:
        result = sqrt_2_with_raises(x)
        assert result == expected


# ---------3 exception with return msg-------------
TEST_SQRT_3_EXCEPTIONS = [
    (-25, "Ошибка! Невозможно найти квадратный корень из отрицательного числа!"),
    ("string", "Ошибка! Вы забыли ввести выражение!"),
    (0, 0.0),
    (4, 2.0),
    (36, 6.0),
    (36.6, 6.04979338490167),
]


@pytest.mark.parametrize("x, ex_outcome", TEST_SQRT_3_EXCEPTIONS)
def test_sqrt_3_with_exceptions(x, ex_outcome):
    result = sqrt_3_with_exceptions(x)
    assert result == ex_outcome


# ------ 4 raises with boolean --------
TEST_SQRT_4_BOOLEAN = [25, -4, 7.567, 3/11, "nine", True, False]


@pytest.mark.parametrize("x", TEST_SQRT_4_BOOLEAN)
def test_raises_boolean(x):
    try:
        # Generating exceptions
        sqrt_3_with_exceptions(x)
    # Checking exceptions, if yes - pass test
    except ValueError:
        assert True
    except TypeError:
        assert True
    except Exception:
        # If any other Exception - test fail
        assert False, "Test failed with not expected exception"
        # Text after assert equalation is good for verification of test fails


def test_greater():
    binary_expression = 2 + 3 / 11
    outcome = sqrt_1(binary_expression)  # 1.507556722888818
    assert outcome > 1.5


def test_less():
    binary_expression = 3 * 7 / 12
    outcome = sqrt_1(binary_expression)  # 1.3228756555322954
    assert outcome < 1.33


def test_not_equal():
    binary_expression = 3 * 7 / 12
    outcome = sqrt_1(binary_expression)  # 1.3228756555322954
    assert outcome != 1.3229
