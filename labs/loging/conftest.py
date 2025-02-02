import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.quit()
