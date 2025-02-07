import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from labs.loging.creds import MAIN_URL, LG_URL, PASSWORD_CREDS, EMAIL_CREDS
from labs.loging.pages.home_page import H2_1, H2_1_TEXT
from labs.loging.pages.login_page import (LoginPage,
                                          H1, H1_TEXT,
                                          EMAIL_FIELD, EMAIL_READONLY,
                                          PASSWORD_FIELD,
                                          CONTINUE_BUTTON, CONTINUE_BUTTON_SPAN,
                                          PASSWORD_LABEL,
                                          SIGNIN_BUTTON, SIGNIN_BUTTON_SPAN)

CONTINUE_BUTTON_TEXT = "Continue"
# PASSWORD_LABEL_TEXT = "Password"
SIGNIN_BUTTON_TEXT = "Sign in"


@pytest.mark.usefixtures("driver")
class TestLoginPageForm:
    def setup_method(self):
        self.login_page = LoginPage(self.driver)

    def test_open_login_page(self):
        self.login_page.open_page(LG_URL)
        h1 = self.login_page.search_element(H1)
        assert h1.text == H1_TEXT, "ERROR! Expected title 'Sign in or register' "

    def test_click_top_account_icon_go_login_page(self):
        self.login_page.open_page(MAIN_URL)

        self.login_page.find_click_on_account_button()
        continue_button_text = self.login_page.search_element(CONTINUE_BUTTON_SPAN).text

        # print user agent
        #self.login_page.get_user_agent()

        assert continue_button_text == CONTINUE_BUTTON_TEXT

    def test_click_continue_button(self):
        self.login_page.open_page(MAIN_URL)
        self.login_page.find_click_on_account_button()

        email_field = self.login_page.search_element(EMAIL_FIELD)
        self.login_page.enter_text(email_field, EMAIL_CREDS)
        print("Email entered")

        continue_button = self.login_page.search_element(CONTINUE_BUTTON)
        self.login_page.click_element(continue_button)
        print("Continue clicked")

        # psw_field = self.login_page.wait_element(PASSWORD_FIELD, 15)
        assert self.login_page.wait_element(PASSWORD_FIELD, 15)

    # @pytest.mark.xfail(reason="Password field not found. TimeoutException")
    def test_click_continue_enter_password(self):
        self.login_page.open_page(MAIN_URL)
        self.login_page.find_click_on_account_button()

        email_field = self.login_page.search_element(EMAIL_FIELD)
        self.login_page.enter_text(email_field, EMAIL_CREDS)
        print("Email entered")

        continue_button = self.login_page.search_element(CONTINUE_BUTTON)
        self.login_page.click_element(continue_button)
        print("Continue clicked")

        # Wait for the password field to be clickable
        # WebDriverWait(self.driver, 15).until(
        #     EC.element_to_be_clickable(PASSWORD_FIELD)
        # )

        # Explicit waits
        wait_psw = WebDriverWait(self.driver, 10)
        wait_psw.until(EC.visibility_of_element_located(PASSWORD_FIELD))

        # Re-find the password field before entering text (in headless mode, elements can change)
        psw_field = self.login_page.search_element(PASSWORD_FIELD)
        print("Password field found")
        self.login_page.enter_text(psw_field, PASSWORD_CREDS)

        assert self.login_page.search_element(SIGNIN_BUTTON)
