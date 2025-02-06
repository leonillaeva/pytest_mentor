from labs.loging.pages.base_page import BasePage  # , ACCOUNT_BUTTON_1
from labs.loging.creds import MAIN_URL
from selenium.webdriver.common.by import By
from selenium import webdriver

H2_1 = (By.XPATH, '//*[@id="z-stt-glados"]/div/div/div[1]/div[1]/div/div[1]/h2')
H2_1_TEXT = 'Our top brands'


class HomePage(BasePage):

    def get_page(self, url):
        self.open_page(url)

    def get_element_text(self, locator):
        element = self.search_element(locator)
        return element.text

    def get_account_button(self):
        """Check the account button and click"""
        self.find_click_on_account_button()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    home_page = HomePage(driver)
    home_page.get_page(MAIN_URL)

    h2_1_text = home_page.get_element_text(H2_1)
    print(h2_1_text)

    cookies = home_page.get_cookies_func()
    print("Cookies:\n ", cookies)

    save_cookies = home_page.save_cookies_pickle()
    # home_page.find_click_on_account_button()

    driver.quit()
