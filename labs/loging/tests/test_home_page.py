from labs.loging.pages.home_page import HomePage


class TestHomePage:

    def setup_method(self):
        self.home_page = HomePage(self.driver)
