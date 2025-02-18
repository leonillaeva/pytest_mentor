import os
from auction_project.locators.locators import LocatorHomePage, LocatorLoginPage, LocatorAccountSettings
from auction_project.creds import USERNAME_EMAIL, PASSWORD

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open_page(self, url_page):
        """Open a page"""
        self.driver.get(url_page)

    def get_page_containing_current_url(self, url, timeout=2):
        """An expectation for checking that the current url contains a case-sensitive substring"""
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def get_current_url(self):
        """Read the current URL from the browser’s address bar"""
        return self.driver.current_url

    def maximize_window_position(self):
        self.driver.maximize_window()

    def wait_element(self, locator, timeout=10):
        """Wait for element appearance on a page"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_all_elements(self, locator, timeout=10):
        """Wait for some elements appearance on a page"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def wait_element_to_be_clickable(self, locator, timeout=10):
        """Used to find the element.
        :return: WebElement : The WebElement once it is located and clickable."""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_text_to_be_present_value(self, locator, expected_text, timeout=3):
        """Used to find the element.
        The text to be present in the element’s value.
        :return: boolean : True when the text is present, False otherwise."""
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_value(locator, expected_text))

    def search_element(self, locator):
        """Find an element on a page"""
        return self.driver.find_element(*locator)

    def search_elements(self, locator):
        """Find elements on a page"""
        return self.driver.find_elements()

    def click_element(self, element):
        """Click on an element"""
        # Find usual modal window with overlap
        # find close button on window with overlap
        # close modal overlap
        element.click()

    def enter_text(self, element, text):
        """Clear a field, enter text into it"""
        element.clear()
        element.send_keys(text)

    def find_click_on_home_signin_button(self):
        """Find Sign In button on the Home page and click on it"""
        signin_button = self.wait_element(LocatorHomePage.HOME_SIGNIN_BUTTON)
        # print("Sign In button is found on the Home page")
        signin_button.click()
        # print("Sign In button is clicked on the Home page")

    def get_property_value_execute_script(self, element, pseudo_element, property_name):
        """The getComputedStyle() method gets the computed CSS properties and values of an HTML element.
            The getComputedStyle() method returns a CSSStyleDeclaration object.

            lock_icon_content = driver.execute_script(
                'return window.getComputedStyle(arguments[0], "::before").getPropertyValue("content");',
                forgot_password_button)
            """

        script = (f"return window.getComputedStyle(arguments[0], '{pseudo_element}'"
                  f").getPropertyValue('{property_name}');")
        return self.driver.execute_script(script, element)

    def normalize_text(self, text):
        """Delete whitespaces before lines"""
        return "\n".join(line.strip() for line in text.splitlines()).strip()

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def login_user(self, url_page):
        self.driver.get(url_page)
        self.driver.maximize_window()
        home_login_button = WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable(LocatorHomePage.HOME_SIGNIN_BUTTON))
        home_login_button.click()

        email_field = WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_element_located(LocatorLoginPage.USERNAME_EMAIL_FIELD))
        email_field.send_keys(USERNAME_EMAIL)

        password_field = WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_element_located(LocatorLoginPage.PASSWORD_FIELD))
        password_field.send_keys(PASSWORD)

        login_signin_button = WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable(LocatorLoginPage.LOGIN_SIGNIN_BUTTON))
        login_signin_button.click()

        account_settings_page = WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_element_located(LocatorAccountSettings.H2_CONTACT_PREFERENCES))
        return account_settings_page

    def get_shadow_root_value(self, locator, locator_shadow):
        """Get shadow root of an element"""
        element_with_shadow_root = self.wait_element(locator, timeout=15).shadow_root
        element_shadow_value = element_with_shadow_root.find_element(*locator_shadow).text
        return element_shadow_value

    # def execute_js_script_click(self, argument, element):
    #     """Executes JavaScript code snippet in the current context.
    #     The click() method simulates a mouse-click on an element.
    #
    #     signin_button = driver.find_element(By.CLASS_NAME, "sign_in")
    #     driver.execute_script("arguments[0].click();", signin_button)
    #
    #     arguments[0] — a list of arguments,
    #     arguments[0] → the first argument (signin_button), passed from Python to JS"""
    #     script = f"{argument}.click();"
    #     self.driver.execute_script(script, element)

    # def execute_js_script_get_value(self, argument, element):
    #     """Executing JavaScript to capture value of element.
    #
    #     Instantly get button text after click
    #     button_text = driver.execute_script("return arguments[0].value;", signin_button)"""
    #     script = f"return {argument}.value;"
    #     return self.driver.execute_script(script, element)
