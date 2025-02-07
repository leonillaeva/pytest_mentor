from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from labs.auction_login.pages.base_page import BasePage
from labs.auction_login.creds import BASE_URL

EMAIL_FIELD = (By.XPATH, '//*[@id="username"]')
PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')

SIGNIN_BUTTON = (By.XPATH, "//div/input[@class='button sign_in']")
SIGNIN_BUTTON_TEXT = 'Sign In'

H2_CONTENT_TITLE = (By.XPATH, "//h2[@class='content_title']")
H2_CON_PREF_TEXT = 'Contact Preferences'


class LoginPage(BasePage):
    def get_page(self, url):
        self.open_page(url)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    # open page
    login_page.get_page(BASE_URL)

    # home_signin_button = login_page.find_click_on_signin_button()
    login_page.find_click_on_signin_button()

    email_field = login_page.search_element(EMAIL_FIELD)
    if email_field:
        print("Email field is found")

    password_field = login_page.search_element(PASSWORD_FIELD)
    if password_field:
        print("Password field is found")

    sign_in_button = login_page.search_element(SIGNIN_BUTTON)
    if sign_in_button:
        print("Sign In button is found")
        # login_page.click_element(sign_in_button)
    else:
        print("Sign In is not found")

    # h2_content_title = login_page.wait_element(H2_CONTENT_TITLE)
    # print(h2_content_title.text.strip())

    driver.quit()
