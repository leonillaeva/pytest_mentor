import pytest
from auction_project.pages.login_page import LoginPage
from auction_project.creds import BASE_URL, LOGIN_URL
from auction_project.locators import HOME_SIGNIN_BUTTON


@pytest.mark.usefixtures("driver")
class TestLoginPage:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)

    # ID: 0001
    def tests_verify_structure_login_page(self):
        # 1 Open the site
        self.login_page.open_page(BASE_URL)
        self.login_page.maximize_window_position()

        # 2 Check 'Sign In' button is present
        signin_button = self.login_page.search_element(HOME_SIGNIN_BUTTON)
        assert signin_button.is_displayed(), "Sign In button should be displayed on the Home Page"

        # 3 Click on 'Sign In' button
        self.login_page.click_element(signin_button)
        current_url = self.login_page.get_current_url()
        assert current_url == LOGIN_URL, f"Login page URL {LOGIN_URL}"


