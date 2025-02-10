import os
from auction_project.locators import HOME_SIGNIN_BUTTON

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

    def get_current_url(self):
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
        element.click()

    def enter_text(self, element, text):
        """Clear a field, enter text into it"""
        element.clear()
        element.send_keys(text)

    def find_click_on_home_signin_button(self):
        """Find Sign In button on the Home page and click on it"""
        signin_button = self.wait_element(HOME_SIGNIN_BUTTON)
        # print("Sign In button is found on the Home page")
        signin_button.click()
        # print("Sign In button is clicked on the Home page")
