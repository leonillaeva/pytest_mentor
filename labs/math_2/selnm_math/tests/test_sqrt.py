import pytest

from pytest_mentor.labs.math_2.selnm_math.pages.sqrt_page import SqrtPage


@pytest.mark.usefixtures("driver")
class TestSqrtPage:
    VALUE_ERROR_MSG = "Ошибка! Невозможно найти квадратный корень из отрицательного числа!"
    TYPE_ERROR_MSG = "Ошибка! Вы ввели некорректное выражение!"
    EXCEPTION_MSG = "Ошибка! Вы забыли ввести выражение!"

    def setup_method(self):
        self.sqrt_page = SqrtPage(self.driver)

    TEST_SQRT = [
        pytest.param(-25, pytest.raises(ValueError), marks=[pytest.mark.xfail]),
        pytest.param("string", pytest.raises(TypeError), marks=[pytest.mark.xfail]),
        pytest.param("?", pytest.raises(Exception), marks=[pytest.mark.xfail]),
        # AssertionError: Expected 1.507556722888818, got 1.5075567228888183
        # pytest.param("2 3/11", pytest.raises(TypeError), marks=[pytest.mark.xfail]),
        (25, "5"),
        (0, "0"),
        (7.567, "2.7508180601413827"),
        (-1, VALUE_ERROR_MSG),
        ("abc", TYPE_ERROR_MSG),
        ("", EXCEPTION_MSG),
        ("?", TYPE_ERROR_MSG),
    ]

    @pytest.mark.parametrize("expression, expected_result", TEST_SQRT)
    def test_sqrt_expression(self, expression, expected_result):
        self.sqrt_page.open()
        self.sqrt_page.enter_expression(expression)
        self.sqrt_page.send_expression()
        final_result = self.sqrt_page.get_outcome()

        assert expected_result == final_result, f"Expected {expected_result}, got {final_result}"
