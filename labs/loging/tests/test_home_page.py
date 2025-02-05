import pytest
from selenium.webdriver.common.by import By
from labs.loging.creds import MAIN_URL
from labs.loging.pages.home_page import HomePage, H2_1, H2_1_TEXT


@pytest.mark.usefixtures("driver")
class TestHomePage:

    def setup_method(self):
        self.home_page = HomePage(self.driver)

    def test_open_home_page(self):
        self.home_page.open_page(MAIN_URL)
        h2_top_brands = self.home_page.search_element(H2_1)
        assert h2_top_brands.text == H2_1_TEXT, "ERROR! Expected title 'Our top brands' "
