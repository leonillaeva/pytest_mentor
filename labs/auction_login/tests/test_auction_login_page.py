import time

import pytest

from labs.auction_login.creds import BASE_URL, USERNAME_EMAIL, PASSWORD
from labs.auction_login.pages.login_page import (LoginPage,
                                                 SIGNIN_BUTTON, SIGNIN_BUTTON_TEXT,
                                                 EMAIL_FIELD, PASSWORD_FIELD,
                                                 H2_CONTENT_TITLE, H2_CON_PREF_TEXT)


@pytest.mark.usefixtures("driver")
class TestLoginPage:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)

    def test_go_to_login_page(self):
        self.login_page.open_page(BASE_URL)
        self.login_page.find_click_on_signin_button()
        signin_button_on_login_page = self.login_page.wait_element(SIGNIN_BUTTON)
        assert signin_button_on_login_page.is_displayed(), f"Error! The Sign In button is not displayed"

    def test_enter_email_psw_signin(self):
        self.login_page.open_page(BASE_URL)
        self.login_page.find_click_on_signin_button()

        email_input = self.login_page.search_element(EMAIL_FIELD)
        self.login_page.enter_text(email_input, USERNAME_EMAIL)

        psw_input = self.login_page.search_element(PASSWORD_FIELD)
        self.login_page.enter_text(psw_input, PASSWORD)

        signin_submit_button = self.login_page.search_element(SIGNIN_BUTTON)
        print(SIGNIN_BUTTON)
        self.login_page.click_element(signin_submit_button)

        h2_content_text = self.login_page.wait_element(H2_CONTENT_TITLE).text.strip()
        assert h2_content_text == H2_CON_PREF_TEXT

    def test_login_find_account_menu_icon(self):
        self.login_page.open_page(BASE_URL)
        self.login_page.maximize_window_position()
        time.sleep(3)
        home_login_button = self.login_page.wait_element(self.login_page.HOME_LOGIN_BUTTON)
        self.login_page.click_element(home_login_button)

        # self.login_page.find_click_on_signin_button()
        # self.login_page.maximize_window_position()
        email_input = self.login_page.search_element(EMAIL_FIELD)
        self.login_page.enter_text(email_input, USERNAME_EMAIL)

        psw_input = self.login_page.search_element(PASSWORD_FIELD)
        self.login_page.enter_text(psw_input, PASSWORD)

        signin_submit_button = self.login_page.search_element(SIGNIN_BUTTON)
        self.login_page.click_element(signin_submit_button)

        top_account_menu_icon = self.login_page.wait_element(self.login_page.TOP_MENU_ACCOUNT_ICON)
        assert top_account_menu_icon.is_enabled(), "ERROR! Account Menu Icon is not enabled"



# 1 go to the login page
# 2 Go to the login page, enter registered: email, password, click Sign In button. Check h2
# 3 Go to the login page, enter registered: email, passw, click Sign In button. Maximize win. Find Account menu button
# 4 Go to the login page, enter registered: email, password, click Sign In button. Maximize win. Find Logout button
# 4 Go to the login page, enter registered: email, password, click Sign In button. Hover Logout button, Logout
