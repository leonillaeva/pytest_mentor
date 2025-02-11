import os
from auction_project.locators import LocatorHomePage

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
        """An expectation for checking that the current url contains a case- sensitive substring"""
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def get_current_url(self):
        """Read the current URL from the browser’s address bar"""
        return self.driver.current_url

    def maximize_window_position(self):
        self.driver.maximize_window()

    def wait_element(self, locator, timeout=3):
        """Wait for element appearance on a page"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def search_element(self, locator):
        """Find an element on a page"""
        return self.driver.find_element(*locator)

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

        script = f"return window.getComputedStyle(arguments[0], '{pseudo_element}').getPropertyValue('{property_name}');"
        return self.driver.execute_script(script, element)
