import pytest
from selenium import webdriver
from labs.loging.creds import MAIN_URL, USER_AGENT


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
    request.cls.driver = driver
    yield driver
    driver.quit()