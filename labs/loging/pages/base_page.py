from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from labs.loging.creds import MAIN_URL


class BasePage:
    ACCOUNT_BUTTON = (By.CLASS_NAME, '#header-user-account-icon > div > a > button')
    HOME_URL = MAIN_URL

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(self.HOME_URL)

    def click_on_account_button(self):
        self.driver.find_element(*self.ACCOUNT_BUTTON).click()

# init driver
# init common locators in header, footer
# common methods: open page, logout, click logo, transition on links
