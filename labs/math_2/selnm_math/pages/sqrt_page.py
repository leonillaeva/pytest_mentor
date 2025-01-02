import re

from pytest_mentor.labs.math_2.selnm_math.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class SqrtPage(BasePage):
    PAGE_URL = r"https://ru.onlinemschool.com/math/assistance/number_theory/square-root-calculator/"
    VALUE_ERROR_MSG = "Ошибка! Невозможно найти квадратный корень из отрицательного числа!"

    EXPRESSION_FIELD = (By.XPATH, "//input[@id='oms_c1']")
    SEND_BUTTON = (By.XPATH, "//input[@id='oms_nabor']")
    OUTCOME = (By.XPATH, "//div[@id='res_main_t']/div/p")
    VALUE_ERROR_WINDOW = (By.CLASS_NAME, "//div[@class='oms_msg_error']")

    def enter_expression(self, expression):
        expression_field = self.driver.find_element(*self.EXPRESSION_FIELD)
        expression_field.clear()
        expression_field.send_keys(expression)

    def send_expression(self):
        self.driver.find_element(*self.SEND_BUTTON).click()

    def get_outcome(self):
        element_outcome = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located(self.OUTCOME))

        full_text = element_outcome.text
        return full_text

    def get_final_result(self):
        full_text = self.get_outcome()
        match = re.findall(r"[-+]?\d*\.\d+|\d+", full_text)
        if match:
            return match[-1]
        return None


if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        sqrt_page = SqrtPage(driver)
        sqrt_page.open()

        expression = 25
        # expression = "2 3/11"
        sqrt_page.enter_expression(expression)
        print(f"Enter {expression}")

        sqrt_page.send_expression()
        full_outcome = sqrt_page.get_outcome()
        print(f"Full outcome: {full_outcome}")

        final_result = sqrt_page.get_final_result()
        print(f"Evaluated final result: {final_result}")
    finally:
        driver.quit()
