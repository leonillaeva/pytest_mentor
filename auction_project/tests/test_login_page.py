import pytest
from auction_project.pages.login_page import LoginPage
from auction_project.creds import BASE_URL, LOGIN_URL
from auction_project.locators import (HOME_SIGNIN_BUTTON,
                                      USERNAME_EMAIL_FIELD, USERNAME_EMAIL_PLACEHOLDER,
                                      PASSWORD_FIELD, PASSWORD_PLACEHOLDER,
                                      LOGIN_SIGNIN_BUTTON,
                                      FORGOT_PASSWORD)


@pytest.mark.usefixtures("driver")
class TestLoginPage:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        # print(dir(self.login_page))

    # ID: 0001
    def tests_verify_structure_login_page(self):
        # 1 Open the site
        self.login_page.open_page(BASE_URL)
        self.login_page.maximize_window_position()

        # 2 Check 'Sign In' button is present
        signin_button = self.login_page.wait_element(HOME_SIGNIN_BUTTON)
        assert signin_button.is_displayed(), "Sign In button should be visible on the Home Page"

        # 3 Click on 'Sign In' button
        self.login_page.click_element(signin_button)

        # Authorisation page opened
        # self.login_page.get_page_containing_current_url(LOGIN_URL)
        assert self.login_page.get_current_url() == LOGIN_URL, f"Login page URL is {LOGIN_URL}"

        # 4 "Check 'Login' field
        # -- "Login field is present
        username_field = self.login_page.search_element(USERNAME_EMAIL_FIELD)
        assert username_field.is_displayed(), "Username field should be visible on the Login Page"
        # -- Login field is empty by default - ?
        assert username_field.get_attribute("value") == '', "Username field should not have a 'value' attribute"
        # -- Login field has  'Email or Username' placeholder
        assert username_field.get_attribute("placeholder").strip() == USERNAME_EMAIL_PLACEHOLDER, \
            f"Placeholder is {USERNAME_EMAIL_PLACEHOLDER} in the Username field"

        # 5 "Check 'Password' field
        # --"Password field is present
        password_field = self.login_page.search_element(PASSWORD_FIELD)
        assert password_field.is_displayed(), "Password field should be visible on the Login Page"

        # -- Password field is empty by default - ?
        assert password_field.get_attribute("value") == '', "Password field should not have a 'value' attribute"
        # -- Password field has 'Password' placeholder
        assert password_field.get_attribute("placeholder").strip() == PASSWORD_PLACEHOLDER, \
            f"Placeholder is {PASSWORD_PLACEHOLDER} in the Password field"

        # 6 Check 'Sign In' button
        # -- "Sign In button is present
        login_signin_button = self.login_page.search_element(LOGIN_SIGNIN_BUTTON)
        assert login_signin_button.is_displayed(), "Sign In button should be visible on the Login page"
        # -- Sign In button is enabled (clickable)"
        assert login_signin_button.is_enabled(), "Sign In button should be clickable on the Login page"

        # 7 Check 'Forgot Password?' button
        # -- "Forgot Password?' button is present
        forgot_password_button = self.login_page.search_element(FORGOT_PASSWORD)
        assert forgot_password_button.is_displayed(), "Forgot Password button should be visible on the Login page"
        # -- 'Forgot Password?' button is enabled (clickable)
        assert forgot_password_button.is_enabled(), "Forgot Password button should be clickable on the Login page"
        # -- ***Check 'Forgot Password?' button has Lock image  (""\f023"")"
        lock_icon_content = self.login_page.get_property_value_execute_script(forgot_password_button,
                                                                              "::before",
                                                                              "content")

        assert lock_icon_content == "\\f023"

