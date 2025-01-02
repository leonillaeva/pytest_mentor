import re

from pytest_mentor.labs.math_2.selnm_math.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class SqrtPage(BasePage):
    PAGE_URL = r"https://ru.onlinemschool.com/math/assistance/number_theory/square-root-calculator/"

    EXPRESSION_FIELD = (By.XPATH, "//input[@id='oms_c1']")
    SEND_BUTTON = (By.XPATH, "//input[@id='oms_nabor']")
    OUTCOME = (By.XPATH, "//div[@id='res_main_t']/div/p")
    ERROR_WINDOW = (By.CLASS_NAME, 'oms_msg_error')

    def enter_expression(self, exprsn):
        expression_field = self.driver.find_element(*self.EXPRESSION_FIELD)
        expression_field.clear()
        expression_field.send_keys(exprsn)

    def send_expression(self):
        self.driver.find_element(*self.SEND_BUTTON).click()

    def get_outcome(self):
        try:
            element_outcome = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.OUTCOME))

            full_text = element_outcome.text

            match = re.findall(r"[-+]?\d*\.\d+|\d+", full_text)
            if match:
                return match[-1]
        except ValueError:
            error_element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.ERROR_WINDOW))
            msg_text = error_element.text
            return msg_text  # "Ошибка! Невозможно найти квадратный корень из отрицательного числа!"
        except TypeError:
            error_element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.ERROR_WINDOW))
            msg_text = error_element.text
            return msg_text  # "Ошибка! Вы ввели некорректное выражение!"
        except Exception:
            error_element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.ERROR_WINDOW))
            msg_text = error_element.text
            return msg_text  # "Ошибка! Вы забыли ввести выражение!"


if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        sqrt_page = SqrtPage(driver)
        sqrt_page.open()

        # expression = 25
        # expression = "2 3/11"
        # expression = "-25" #  "Ошибка! Невозможно найти квадратный корень из отрицательного числа!"
        # expression = -25 # -> Ошибка! Вы ввели некорректное выражение! -? exp "Ошибка! Невозможно найти квадратный корень из отрицательного числа!"
        expression = ''  # -> "Ошибка! Вы забыли ввести выражение!"
        # expression = 'string'  # -> Ошибка! Вы ввели некорректное выражение!

        sqrt_page.enter_expression(expression)
        print(f"Enter {expression}")

        sqrt_page.send_expression()
        outcome = sqrt_page.get_outcome()

        print(f"Evaluated final result: {outcome}")
    finally:
        driver.quit()
