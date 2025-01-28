from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    SIGN_UP_BUTTON = (By.ID, "sign-up-btn")

    def go_to_sign_up_page(self):
        self.click_element(self.SIGN_UP_BUTTON)
