from selenium.webdriver.common.by import By


class LocatorAuctionEventsPage:
    # H1
    H1_AUCTION_EVENTS = (By.XPATH, "//h1[text()='Auction Events']")

    CHECKBOX_LIMIT_MY_AUCTIONS = (By.XPATH, "//div[@class='my-auctions-filter']//input")

    # CALENDAR, PICKER
    CALENDAR = (By.XPATH, "//input[@id='input-9']")
    CALENDAR_PICKER = (By.XPATH, "//div[contains(@class, 'v-picker__body')]")
    CALENDAR_SHADOW_VALUE = (By.CSS_SELECTOR, "div")
    CALENDAR_DAYS = (By.XPATH, "//div[@class='v-btn__content']")
    CALENDAR_PICKER_HEADER = (By.XPATH, "//div[@class='accent--text']/button")
    ACTIVE_DAY_PICKER = (By.XPATH, "//button[@class='v-btn v-date-picker-table__current "
                                   "v-btn--active v-btn--text v-btn--rounded theme--light accent']/div")

    LEFT_PICKER_ARROW = (By.XPATH, "//i[@class='v-icon notranslate mdi mdi-chevron-left theme--light']")
    RIGHT_PICKER_ARROW = (By.XPATH, "//i[@class='v-icon notranslate mdi mdi-chevron-right theme--light']")

    # EVENTS BLOCK
    BLOCK_EVENTS = (By.XPATH, "//ul[@class='days']")
    DAY_BLOCKS = (By.XPATH, "//ul[@class='days']//li[contains(@class, 'day')]")
    AUCTION_DAY_H2_FULL_PATH = (By.XPATH, "//ul[@class='days']//li[contains(@class, 'day')]//h2")
    AUCTION_DAY_H2 = (By.XPATH, ".//h2")
    # AUCTION_DAY_LI = (By.XPATH, "//ul[@class='days']//li[contains(@class, 'day')]//ul[@class='events']//li")
    AUCTION_DAY_LI = (By.XPATH, ".//ul[@class='events']//li[@class='auction']")
    # AUCTION_NO_EVENTS = (By.XPATH, "//ul[@class='days']//li[contains(@class, 'day')]"
    #                                "//ul[@class='events']//li[@class='no_events']")
    # AUCTION_NUMBER = (By.XPATH, "//ul[@class='days']//li[contains(@class, 'day')]"
    #                            "//ul[@class='events']//li//span[@class='hidden_count']")
    AUCTION_NUMBER = (By.XPATH, ".//span[@class='hidden_count']")
    AUCTION_NO_EVENTS = (By.XPATH, ".//li[@class='no_events']")
    NO_EVENTS_TEXT = "No Events Today"

    # ------0009
    CONTENT_EVENTS_WITH_CHECKBOX = (By.XPATH, ".//li[contains(@class, 'no_events')]")
    # AUCTION_ALL_EVENTS_WITH_CHECKBOX = (By.XPATH, "//ul[@class='events']/li")

    RIGHT_EVENTS_BLOCK_ARROWS = (By.XPATH, "//a[@class='next']/i")
    LEFT_EVENTS_BLOCK_ARROWS = (By.XPATH, "//a[@class='back']/i")
    LIST_BLOCK_DATES = (By.XPATH, "//ul/li/h2")

    # TODAY BUTTON
    TODAY_BUTTON_ENABLED = (By.XPATH, "//a[@class = 'button secondary']")
    TODAY_BUTTON_DISABLED = (By.XPATH, "//a[@class ='button secondary disabled']")

