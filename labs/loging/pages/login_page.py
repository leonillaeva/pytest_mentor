from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from base_page import BasePage
from labs.loging.creds import LG_URL


class LoginPage(BasePage):
    LOGIN_URL = LG_URL
    H1 = (By.XPATH, '//*[@id="theme-wrapper"]/main/section[1]/section[1]/h1')
    H1_TEXT = 'Sign in or register'
    EMAIL_FIELD = (By.XPATH, '//*[@id="lookup-email"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="theme-wrapper"]/main/section[1]/form/button')

