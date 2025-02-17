import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from auction_project.creds import BASE_URL, USER_AGENT, USERNAME_EMAIL, PASSWORD
from auction_project.locators.locators import LocatorHomePage, LocatorLoginPage, LocatorAccountSettings
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="class")
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-agent={USER_AGENT}")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Remove Selenium detection
    options.add_argument("--incognito")  # Use incognito mode
    options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Exclude automation switches
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """
    })
    driver.execute_cdp_cmd(
        'Network.setExtraHTTPHeaders',
        {"headers": {
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": USER_AGENT,
        }}
    )
    request.cls.driver = driver  # bind the driver to class
    yield driver
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def clean_cookies(driver):  # Pass driver
    """Clear all cookies after each test"""
    yield
    driver.delete_all_cookies()


@pytest.fixture(scope="function")
def login_user(driver):
    """Log in as a user before each test."""
    driver.get(BASE_URL)
    driver.maximize_window()

    home_login_button = WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable(LocatorHomePage.HOME_SIGNIN_BUTTON))
    home_login_button.click()

    email_field = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located(LocatorLoginPage.USERNAME_EMAIL_FIELD))
    email_field.send_keys(USERNAME_EMAIL)

    password_field = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located(LocatorLoginPage.PASSWORD_FIELD))
    password_field.send_keys(PASSWORD)

    login_signin_button = WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable(LocatorLoginPage.LOGIN_SIGNIN_BUTTON))
    login_signin_button.click()

    WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located(LocatorAccountSettings.H2_CONTACT_PREFERENCES))

    yield driver  # return logged in driver


@pytest.fixture(scope='function')
def wait_click_account_settings_cancel_button(driver):
    """Wait and click 'Cancel' button on Account Settings page and go to Auction Events page."""
    cancel_bottom_button = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located(LocatorAccountSettings.CANCEL_BOTTOM_BUTTON))

    WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(cancel_bottom_button))
    cancel_bottom_button.click()
    yield
