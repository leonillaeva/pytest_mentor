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
        # # AssertionError: Expected 1.507556722888818, got 1.507556722888818
        pytest.param("2 3/11", "1.5075567228888183", marks=[pytest.mark.xfail]),
        (25, "5"),
        (0, "0"),
        (7.567, "2.7508180601413827"),
    ]

    @pytest.mark.parametrize("expression, expected_result", TEST_SQRT)
    def test_sqrt_expression_valid_cases(self, expression, expected_result):
        self.sqrt_page.open()
        self.sqrt_page.enter_expression(expression)
        self.sqrt_page.send_expression()
        final_result = self.sqrt_page.get_outcome_numbers()

        assert expected_result == final_result, f"Expected {expected_result}, got {final_result}"

    def test_sqrt_expression_negative_value_error(self):
        self.sqrt_page.open()
        self.sqrt_page.enter_expression(-1)
        self.sqrt_page.send_expression()
        final_result = self.sqrt_page.get_outcome_pop_up_message()

        assert self.VALUE_ERROR_MSG == final_result, f"Expected {self.VALUE_ERROR_MSG}, got {final_result}"


    def test_sqrt_expression_negative_type_error(self):
        self.sqrt_page.open()
        self.sqrt_page.enter_expression("abc")
        self.sqrt_page.send_expression()
        final_result = self.sqrt_page.get_outcome_pop_up_message()

        assert self.TYPE_ERROR_MSG == final_result, f"Expected {self.TYPE_ERROR_MSG}, got {final_result}"


    def test_sqrt_expression_negative_type_error_empty_message(self):
        self.sqrt_page.open()
        self.sqrt_page.enter_expression("")
        self.sqrt_page.send_expression()
        final_result = self.sqrt_page.get_outcome_pop_up_message()

        assert self.EXCEPTION_MSG == final_result, f"Expected {self.EXCEPTION_MSG}, got {final_result}"