import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from auction_project.pages.login_page import LoginPage
from auction_project.creds import BASE_URL, LOGIN_URL, USERNAME_EMAIL, PASSWORD, FORGOT_PASSWORD_URL
from auction_project.locators.locators import LocatorHomePage, LocatorLoginPage, LocatorAccountSettings


@pytest.mark.usefixtures("driver")
class TestLoginPage:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        # print(dir(self.login_page))

    # ID: 0001
    def tests_0001_verify_structure_login_page(self):
        """Verify structure of login page."""
        # 1 Open the site
        self.login_page.open_page(BASE_URL)
        self.login_page.maximize_window_position()

        # 2 Check 'Sign In' button is present
        signin_button = self.login_page.wait_element(LocatorHomePage.HOME_SIGNIN_BUTTON)
        assert signin_button.is_displayed(), "Sign In button should be visible on the Home Page"

        # 3 Click on 'Sign In' button
        self.login_page.click_element(signin_button)

        # Authorisation page opened
        # self.login_page.get_page_containing_current_url(LOGIN_URL)
        assert self.login_page.get_current_url() == LOGIN_URL, f"Login page URL is {LOGIN_URL}"
        # alternative checking that page with login is opened is to check
        # web element, which we need
        login_page_el = self.login_page.wait_element(LocatorLoginPage.LOGIN_WINDOW)
        assert login_page_el.is_displayed(), "Authorisation page did not opened"

        # 4 "Check 'Login' field
        # -- "Login field is present
        username_field = self.login_page.search_element(LocatorLoginPage.USERNAME_EMAIL_FIELD)
        assert username_field.is_displayed(), "Username field should be visible on the Login Page"
        # -- Login field is empty by default - ?
        assert username_field.get_attribute("value") == '', "Username field should not have a 'value' attribute"
        # -- Login field has  'Email or Username' placeholder
        assert username_field.get_attribute("placeholder").strip() == LocatorLoginPage.USERNAME_EMAIL_PLACEHOLDER, \
            f"Placeholder is {LocatorLoginPage.USERNAME_EMAIL_PLACEHOLDER} in the Username field"

        # 5 "Check 'Password' field
        # --"Password field is present
        password_field = self.login_page.search_element(LocatorLoginPage.PASSWORD_FIELD)
        assert password_field.is_displayed(), "Password field should be visible on the Login Page"

        # -- Password field is empty by default - ?
        assert password_field.get_attribute("value") == '', "Password field should not have a 'value' attribute"
        # -- Password field has 'Password' placeholder
        assert password_field.get_attribute("placeholder").strip() == LocatorLoginPage.PASSWORD_PLACEHOLDER, \
            f"Placeholder is {LocatorLoginPage.PASSWORD_PLACEHOLDER} in the Password field"

        # 6 Check 'Sign In' button
        # -- "Sign In button is present
        login_signin_button = self.login_page.search_element(LocatorLoginPage.LOGIN_SIGNIN_BUTTON)
        assert login_signin_button.is_displayed(), "Sign In button should be visible on the Login page"
        # -- Sign In button is enabled (clickable)"
        assert login_signin_button.is_enabled(), "Sign In button should be clickable on the Login page"
        # this is fine. Just alternative approach FYI (not always needed):
        # WebDriverWait(self.driver, 5).until(
        #  EC.element_to_be_clickable(LocatorLoginPage.LOGIN_SIGNIN_BUTTON))

        # 7 Check 'Forgot Password?' button
        # -- "Forgot Password?' button is present
        forgot_password_button = self.login_page.search_element(LocatorLoginPage.FORGOT_PASSWORD)
        assert forgot_password_button.is_displayed(), "Forgot Password button should be visible on the Login page"
        # -- 'Forgot Password?' button is enabled (clickable)
        assert forgot_password_button.is_enabled(), "Forgot Password button should be clickable on the Login page"
        # -- ***Check 'Forgot Password?' button has Lock image  (""\f023"")"
        lock_icon_content = self.login_page.get_property_value_execute_script(forgot_password_button,
                                                                              "::before",
                                                                              "content")

        assert lock_icon_content == '"\uf023"'

        # 8 Check 'Sign Up Now!' button
        # -- Check 'Sign Up Now!' button is present
        signup_now_button = self.login_page.search_element(LocatorLoginPage.SIGNUP_NOW_BUTTON)
        assert signup_now_button.is_displayed(), "'Sign Up Now!' button should be visible on the Login page"
        # Check 'Sign Up Now!' button is enabled (clickable)
        assert signup_now_button.is_enabled(), "'Sign Up Now!' button should be clickable on the Login page"
        # ***Check  'Sign Up Now!' button has Pencil symbol  ("\f040")
        pencil_icon_content = self.login_page.get_property_value_execute_script(signup_now_button,
                                                                                "::before",
                                                                                "content")
        assert pencil_icon_content == '"\uf040"'

    def test_0002_verify_user_login_success(self):
        """Verify user login success"""

        # 1 Open the site
        self.login_page.open_page(BASE_URL)
        self.login_page.maximize_window_position()

        # 2 Check 'Sign In' button is present and clickable
        home_signin_button = self.login_page.wait_element_to_be_clickable(LocatorHomePage.HOME_SIGNIN_BUTTON)

        # 3 Click on 'Sign In' button
        self.login_page.click_element(home_signin_button)

        # -- Authorisation page opened
        login_form = self.login_page.wait_element(LocatorLoginPage.LOGIN_WINDOW)
        assert login_form.is_displayed(), "Authorisation page was not opened"

        # 4 Enter user and password
        # -- * User is entered and shown, Via selenium WebDriver get value of entered email text
        username_field = self.login_page.search_element(LocatorLoginPage.USERNAME_EMAIL_FIELD)
        self.login_page.enter_text(username_field, USERNAME_EMAIL)
        entered_username_text = username_field.get_attribute("value")

        assert entered_username_text == USERNAME_EMAIL, (f"Expected username is {USERNAME_EMAIL}"
                                                         f", but got {entered_username_text}")
        # -- ** Password is entered as dots (hidden),
        # -- Via selenium WebDriver automation need to check that entered password are dots (or hidden)
        password_field = self.login_page.search_element(LocatorLoginPage.PASSWORD_FIELD)
        self.login_page.enter_text(password_field, PASSWORD)
        assert password_field.get_attribute("type") == "password", "Password is not displayed in dots"
        assert password_field.get_attribute("value") == PASSWORD, "Gotten password is not the same as entered"

        # 5 Click on 'Sign In' button
        # 'Sign In' button is changed to 'Signing In…' button
        login_signin_button = self.login_page.search_element(LocatorLoginPage.LOGIN_SIGNIN_BUTTON)
        self.login_page.click_element(login_signin_button)
# 1 ----------after click Signing In...-
        # self.login_page.wait_text_to_be_present_value(LocatorLoginPage.LOGIN_SIGNIN_BUTTON,
        #                                               LocatorLoginPage.LG_SIGNIN_BUTTON_TEXT_AFTER_CLICK)
        # login_signin_button = self.login_page.search_element(LocatorLoginPage.LOGIN_SIGNIN_BUTTON)
        #
        # changed_text = login_signin_button.get_attribute("value")
        # assert changed_text == LocatorLoginPage.LG_SIGNIN_BUTTON_TEXT_AFTER_CLICK

        # * User is redirected to Contact Preferences page
        h2_contact_preferences = self.login_page.search_element(LocatorAccountSettings.H2_CONTACT_PREFERENCES).text
        assert h2_contact_preferences == LocatorAccountSettings.H2_CONTACT_PREFERENCES_TEXT

    def test_0003_check_login_error(self):
        """Verify login error modal window"""
        # 1 Open the site
        self.login_page.open_page(BASE_URL)
        self.login_page.maximize_window_position()

        # 2 Check 'Sign In' button is present and clickable
        home_signin_button = self.login_page.wait_element(LocatorHomePage.HOME_SIGNIN_BUTTON)
        self.login_page.wait_element_to_be_clickable(home_signin_button)

        # 3 Click on 'Sign In' button
        self.login_page.click_element(home_signin_button)

        # 4 "Enter invalid user and password, (Or leave empty)
        login_signin_button = self.login_page.search_element(LocatorLoginPage.LOGIN_SIGNIN_BUTTON)
        self.login_page.click_element(login_signin_button)

        # -- Invalid Username or Password modal window appeared
        dialog_modal_window = self.login_page.search_element(LocatorLoginPage.DIALOG_MODAL_WINDOW)
        assert dialog_modal_window.is_displayed(), "The 'Invalid Username or Password' modal window is not displayed"

        # 5 "Check error window header text
        # "Error window title text is shown
        window_title = self.login_page.search_element(LocatorLoginPage.MODAL_WINDOW_TITLE)
        assert window_title.is_displayed(), "The modal window title is not shown"
        # Error window title text is: "Invalid Username or Password"
        assert window_title.text == LocatorLoginPage.MOD_WIN_TITLE_TEXT, \
            f"The title should be shown as {LocatorLoginPage.MOD_WIN_TITLE_TEXT}"

        # 6 Check error window description text
        # -- Error window description text is shown
        window_description = self.login_page.search_element(LocatorLoginPage.WINDOW_DESCRIPTION)
        assert window_description.is_displayed(), "The Description block is not shown on the Modal Window"
        # -- Error window description text is:
        # "That username and password does not appear to match any accounts on record.
        # Check to make sure you've entered your case-sensitive password correctly.
        # If the problem persists, you may also make a request for your password to be reset."

        actual_text = self.login_page.normalize_text(window_description.text)
        expected_text = self.login_page.normalize_text(LocatorLoginPage.WINDOW_DESCRIPTION_TEXT)

        assert actual_text == expected_text, f"The Description text is not matched to the expected text {expected_text}"

        # 7 Check description text has link to forgotten_password page
        # -- in text 'make a request for your password to be reset'
        window_forgot_password_link = self.login_page.search_element(
            LocatorLoginPage.WINDOW_FORGOT_PASSWORD_LINK_TEXT).get_attribute("href")
        assert window_forgot_password_link == FORGOT_PASSWORD_URL, \
            f"Forgot Password URL: {FORGOT_PASSWORD_URL}, got {window_forgot_password_link}"

        # 8 Check Red 'X' Icon is shown in the error window
        red_x_icon_block = self.login_page.search_element(LocatorLoginPage.RED_X_BUTTON_MODAL_WINDOW)
        red_x_icon_content = self.login_page.get_property_value_execute_script(red_x_icon_block,
                                                                               "::before",
                                                                               "content")

        assert red_x_icon_content == '"\uf057"', "Red 'X' icon is not displayed correctly!"  # ""

        red_x_icon_color = self.login_page.get_property_value_execute_script(
            red_x_icon_block, "::before", "color")
        assert red_x_icon_color == 'rgb(229, 77, 66)', "Incorrect red color for 'X' icon!"

# 2 -----------red x button img---------- assert 'none'--
#         red_x_icon_img = self.login_page.get_property_value_execute_script(
#             red_x_icon_block, "", "background-image")
#         assert red_x_icon_img == 'https://www.edgepipeline.com/images/session_messenger/stop-red.png', \
#             "Image is not found for red 'X' icon!"

        # 9 Check Error window has close ('x') button at top right corner
        close_button = self.login_page.search_element(LocatorLoginPage.CLOSE_BUTTON_MODAL_WINDOW)
        assert close_button.is_displayed(), "Close button is not displayed."

        # 10 Check 'Got it' button
        # -- 'Got it' button is present
        got_it_button = self.login_page.search_element(LocatorLoginPage.GOT_IT_BUTTON)
        assert got_it_button.is_displayed(), "The 'Got it' button is not displayed"
        # -- 'Got it' button is enabled
        assert got_it_button.is_enabled(), "The 'Got it' button is not enabled"

        # 11 Click on 'Got it' button, User returns to login page
        self.login_page.click_element(got_it_button)
        login_window = self.login_page.search_element(LocatorLoginPage.LOGIN_WINDOW)
        assert login_window.is_displayed(), "The login form is not displayed"
