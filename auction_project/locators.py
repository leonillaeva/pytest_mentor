from selenium.webdriver.common.by import By

# HOME PAGE
HOME_SIGNIN_BUTTON = (By.XPATH, '//a[text()="Sign In"]')

# LOGIN PAGE
# USERNAME_EMAIL_FIELD = (By.XPATH, "//input[@id='username']")
USERNAME_EMAIL_FIELD = (By.ID, "username")
USERNAME_EMAIL_PLACEHOLDER = "Email or Username"

PASSWORD_FIELD = (By.ID, "password")
PASSWORD_PLACEHOLDER = "Password"

LOGIN_SIGNIN_BUTTON = (By.XPATH, "//input[@value='Sign In']")

FORGOT_PASSWORD = (By.XPATH, '//ul[@class="utility"]/li[1]/a')
