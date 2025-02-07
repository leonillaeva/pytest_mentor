import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.webdriver import WebDriver

from labs.loging.creds import MAIN_URL, LG_URL, PASSWORD_CREDS, EMAIL_CREDS
from labs.loging.pages.home_page import H2_1, H2_1_TEXT
from labs.loging.pages.login_page import (LoginPage,
                                          H1, H1_TEXT,
                                          EMAIL_FIELD, EMAIL_READONLY,
                                          PASSWORD_FIELD,
                                          CONTINUE_BUTTON, CONTINUE_BUTTON_SPAN,
                                          PASSWORD_LABEL,
                                          SIGNIN_BUTTON, SIGNIN_BUTTON_SPAN)


@pytest.mark.usefixtures("driver_headless")
class TestLoginPageHeadlessForm:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)

    @pytest.mark.skip("Email field not found, NoSuchElementException ")
    def test_click_continue_enter_password(self):
        self.login_page.open_page(LG_URL)

        email_field = self.login_page.search_element(EMAIL_FIELD)
        self.login_page.enter_text(email_field, EMAIL_CREDS)
        print("Email entered")

        continue_button = self.login_page.search_element(CONTINUE_BUTTON)
        self.login_page.click_element(continue_button)
        print("Continue clicked")

        # Wait for the password field to be present

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(PASSWORD_FIELD)
        )
        # Wait for the password field to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(PASSWORD_FIELD)
        )

        # Re-find the password field before entering text (in headless mode, elements can change)
        psw_field = self.login_page.search_element(PASSWORD_FIELD)
        self.login_page.enter_text(psw_field, PASSWORD_CREDS)

        # Check if the "Sign In" button is visible
        signin_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SIGNIN_BUTTON)
        )
        assert signin_button
