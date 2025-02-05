from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from labs.loging.pages.base_page import BasePage
from labs.loging.creds import LG_URL

H1 = (By.XPATH, '//*[@id="theme-wrapper"]/main/section[1]/section[1]/h1')
H1_TEXT = 'Sign in or register'

EMAIL_FIELD = (By.XPATH, '//*[@id="lookup-email"]')
EMAIL_READONLY = (By.XPATH, '//*[@id="login-email"]')

PASSWORD_FIELD = (By.XPATH, '//*[@id="login-password"]')

CONTINUE_BUTTON = (By.XPATH, "//button[@data-testid='verify-email-button']")
CONTINUE_BUTTON_SPAN = (By.XPATH, "//button[@data-testid='verify-email-button']/span")

PASSWORD_LABEL = (By.XPATH, '//label[@for="login-password"]')

SIGNIN_BUTTON = (By.XPATH, '//form[@name="login"]//button[@data-name="sso_login"]')
SIGNIN_BUTTON_SPAN = (By.XPATH, '//form[@name="login"]//button[@data-name="sso_login"]/span')


class LoginPage(BasePage):
    def get_page(self, url):
        self.open_page(url)

    def presence_element(self, locator):
        return self.wait_element(locator)

    def get_element_text(self, locator):
        element = self.search_element(locator)
        return element.text


if __name__ == "__main__":
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    # open page
    login_page.get_page(LG_URL)

    # section h1, get h1 text
    h1_text = login_page.get_element_text(H1)
    print(h1_text)

    # find email field
    email_field = login_page.presence_element(EMAIL_FIELD)
    if email_field:
        print("Email field is found")

    # find Submit button
    submit_button = login_page.presence_element(CONTINUE_BUTTON)
    if submit_button:
        print("Continue button  is found")

    driver.quit()
