from .base_page import BasePage
from selenium.webdriver.common.by import By


class SqrtPage(BasePage):
    PAGE_URL = r"https://ru.onlinemschool.com/math/assistance/number_theory/square-root-calculator/"

    EXPRESSION_FIELD = (By.XPATH, "//input[@id='oms_c1']")
    SEND_BUTTON = (By.XPATH, "//input[@id='oms_nabor']")
    OUTCOME = (By.XPATH, "//div[@id='res_main_t']/div/p/text()")
