from selenium.webdriver.common.by import By


# HOME PAGE
class LocatorHomePage:
    HOME_SIGNIN_BUTTON = (By.XPATH, '//a[text()="Sign In"]')


# LOGIN PAGE
class LocatorLoginPage:
    LOGIN_WINDOW = (By.XPATH, '//div[@id="login_box"]')
    USERNAME_EMAIL_FIELD = (By.ID, "username")
    USERNAME_EMAIL_PLACEHOLDER = "Email or Username"

    PASSWORD_FIELD = (By.ID, "password")
    PASSWORD_PLACEHOLDER = "Password"

    LOGIN_SIGNIN_BUTTON = (By.XPATH, "//input[@value='Sign In']")
    LOGIN_SIGNIN_BUTTON_TEXT = "Sign In"
    LG_SIGNIN_BUTTON_TEXT_AFTER_CLICK = "Signing In..."

    FORGOT_PASSWORD = (By.XPATH, '//ul[@class="utility"]/li[1]/a')
    SIGNUP_NOW_BUTTON = (By.XPATH, '//ul[@class="utility"]/li[2]/a')

    DIALOG_MODAL_WINDOW = (By.CSS_SELECTOR, "body > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all")
    MODAL_WINDOW_TITLE = (By.ID, 'ui-dialog-title-1')
    MOD_WIN_TITLE_TEXT = 'Invalid Username or Password'
    WINDOW_DESCRIPTION = (By.XPATH, "//div[@class='message']/div")

    WINDOW_DESCRIPTION_TEXT = """
    That username and password does not appear to match any accounts on record.
    Check to make sure you've entered your case-sensitive password correctly.
    If the problem persists, you may also make a request for your password to be reset."""

    WINDOW_FORGOT_PASSWORD_LINK_TEXT = (By.LINK_TEXT, 'make a request for your password to be reset')
    RED_X_BUTTON_MODAL_WINDOW = (By.XPATH, "//div[@class='message']")
    CLOSE_BUTTON_MODAL_WINDOW = (By.XPATH, "//span[@class = 'ui-icon ui-icon-closethick']")
    GOT_IT_BUTTON = (By.XPATH, "//button[text()='Got it']")


class LocatorAccountSettings:
    H2_CONTACT_PREFERENCES = (By.XPATH, "//h2[text()='Contact Preferences']")
    H2_CONTACT_PREFERENCES_TEXT = 'Contact Preferences'
