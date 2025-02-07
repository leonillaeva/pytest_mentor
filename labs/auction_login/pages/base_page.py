import pickle
import os

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver


class BasePage:
    LOGIN_BUTTON = (By.XPATH, '//*[@id="welcome"]//a[@href="/components/login"]')
    TOP_ACCOUNT_BUTTON = (By.XPATH, "//*[@id='page_header']//div[@class='menu my_account']")
    TOP_MENU_ACCOUNT_ICON = (By.XPATH, '//*[@id="page_header"]//div[@class="menu my_account"]/a')
    LOGOUT_LINK = (By.XPATH, "//a[@href='/logout/']")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open_page(self, url_page):
        """Open a page"""
        self.driver.get(url_page)

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
        element.clear()
        element.send_keys(text)

    def find_click_on_signin_button(self):
        """Find Sign In button on the Home page and click on it"""
        signin_button = self.search_element(self.LOGIN_BUTTON)
        # print("Sign In button is found on the Home page")
        signin_button.click()
        # print("Sign In button is clicked on the Home page")

    def find_click_top_menu_account_arrow(self):
        """Hover the cursor on an element and click on other element."""
        top_account_menu = self.search_element(self.TOP_ACCOUNT_BUTTON)
        ActionChains(self.driver).move_to_element(top_account_button).perform()
        # self.click_element(click_locator)

    # def click_logout_link(self):
    #     """Logout function on the site"""
    #     account_button = self.driver.find_element(*self.ACCOUNT_BUTTON)
    #     ActionChains(self.driver).move_to_element(account_button).perform()
    #     # logout_link = self.driver.find_element(*self.LOGOUT_LINK)
    #     # logout_link.click()
    #     self.click_element(*self.LOGOUT_LINK)
    #     # self.click_element(self.LOGOUT_LINK)

    def find_hover_element(self, hover_locator):
        """Find element and hover over it"""
        hover_element = self.search_element(hover_locator)
        ActionChains(self.driver).move_to_element(hover_element).perform()

    def hover_and_click(self, hover_locator, click_locator):
        """Hover the cursor on an element and click on other element."""
        hover_element = self.search_element(hover_locator)
        ActionChains(self.driver).move_to_element(hover_element).perform()
        self.click_element(click_locator)

    def get_user_agent(self):
        """# Get user Agent with execute_script"""
        user_agent = self.driver.execute_script("return navigator.userAgent")
        print("User agent:", user_agent)

    def get_cookies_func(self):
        return self.driver.get_cookies()

    def save_cookies_pickle(self):
        cookies = self.get_cookies_func()
        if cookies:
            cookies_dir = os.path.join(os.getcwd(), "cookies")
            os.makedirs(cookies_dir, exist_ok=True)  # Create directory if it does not exist
            cookies_file_path = os.path.join(cookies_dir, "cookies.pkl")
            try:
                with open(cookies_file_path, "wb") as cookies_file:
                    pickle.dump(cookies, cookies_file)
                print("Cookies saved successfully.")
            except Exception as e:
                print(f"Error saving cookies: {e}")
        else:
            print("No cookies found to save.")

    def maximize_window_position(self):
        self.driver.maximize_window()

# init driver
# init common locators in header, footer
# common methods: open page, logout, click logo, transition on links
