from selenium.webdriver.common.by import By


class LocatorAuctionEventsPage:
    H1_AUCTION_EVENTS = (By.XPATH, "//h1[text()='Auction Events']")
    CALENDAR = (By.XPATH, "//input[@id='input-9']")
    CALENDAR_SHADOW_VALUE = (By.CSS_SELECTOR, "div")
