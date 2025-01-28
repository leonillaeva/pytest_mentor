from selenium.webdriver.common.by import By
from .base_page import BasePage


class SignUpPage(BasePage):
    TITLE = (By.TAG_NAME, "h1")
    FIRSTNAME_FIELD = (By.ID, "firstname")
    LASTNAME_FIELD = (By.ID, "lastname")
    PASSWORD_FIELD = (By.ID, "password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "confirm-password")
    AGE_FIELD = (By.ID, "age")
    ROLE_DROPDOWN = (By.ID, "role")
    TEACHER_CODE_POPUP = (By.ID, "popup")
    TEACHER_CODE_FIELD = (By.ID, "verification-code")
    POPUP_CLOSE_BUTTON = (By.ID, "close-popup")
    SIGN_UP_BUTTON = (By.ID, "sign-up-submit")

    def fill_form(self, firstname, lastname, password, confirm_password, age, role, verification_code=None):
        self.enter_text(self.FIRSTNAME_FIELD, firstname)
        self.enter_text(self.LASTNAME_FIELD, lastname)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.enter_text(self.CONFIRM_PASSWORD_FIELD, confirm_password)
        self.enter_text(self.AGE_FIELD, age)
        self.select_role(role)
        if role == "teacher" and verification_code:
            self.enter_verification_code(verification_code)

    def select_role(self, role):
        dropdown = self.find_element(self.ROLE_DROPDOWN)
        dropdown.click()
        dropdown.find_element(By.XPATH, f"//option[text()='{role}']").click()

    def enter_verification_code(self, code):
        self.click_element(self.TEACHER_CODE_POPUP)
        self.enter_text(self.TEACHER_CODE_FIELD, code)
        self.click_element(self.POPUP_CLOSE_BUTTON)
