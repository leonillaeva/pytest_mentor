from selenium.webdriver.common.by import By


class LocatorAuctionEventsPage:
    H1_AUCTION_EVENTS = (By.XPATH, "//h1[text()='Auction Events']")
    CALENDAR = (By.XPATH, "//input[@id='input-9']")
    CALENDAR_PICKER = (By.XPATH, "//div[contains(@class, 'v-picker__body')]")
    CALENDAR_SHADOW_VALUE = (By.CSS_SELECTOR, "div")
    CALENDAR_DAYS = (By.XPATH, "//div[@class='v-btn__content']")
    CALENDAR_PICKER_HEADER = (By.XPATH, "//div[@class='accent--text']/button")

    CHECKBOX_LIMIT_MY_AUCTIONS = (By.XPATH, "//div[@class='my-auctions-filter']//input")
    BLOCK_EVENTS = (By.XPATH, "//ul[@class='days']")
    DAY_BLOCKS = (By.XPATH, "//ul[@class='days']//li[contains(@class, 'day')]")
    # AUCTION_DAY_H2 = (By.XPATH, "//ul[@class='days']//li[contains(@class, 'day')]//h2")
    AUCTION_DAY_H2 = (By.XPATH, ".//h2")
    # AUCTION_DAY_LI = (By.XPATH, "//ul[@class='days']//li[contains(@class, 'day')]//ul[@class='events']//li")
    AUCTION_DAY_LI = (By.XPATH, ".//ul[@class='events']//li")
    # AUCTION_NO_EVENTS = (By.XPATH, "//ul[@class='days']//li[contains(@class, 'day')]"
    #                                "//ul[@class='events']//li[@class='no_events']")
    # AUCTION_NUMBER = (By.XPATH, "//ul[@class='days']//li[contains(@class, 'day')]"
    #                            "//ul[@class='events']//li//span[@class='hidden_count']")
    AUCTION_NUMBER = (By.XPATH, ".//span[@class='hidden_count']")
    AUCTION_NO_EVENTS = (By.XPATH, "//ul[@class='events']//li[@class='no_events']")
    NO_EVENTS_TEXT = "No Events Today"
