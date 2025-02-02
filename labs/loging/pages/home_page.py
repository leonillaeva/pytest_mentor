from base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    H2_1 = (By.XPATH, '//*[@id="z-stt-glados"]/div/div/div[1]/div[1]/div/div[1]/h2')
    H2_1_TEXT = 'Our top brands'
