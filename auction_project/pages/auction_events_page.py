from selenium.webdriver.common.by import By

from datetime import date

from auction_project.pages.base_page import BasePage
from auction_project.creds import BASE_URL
from auction_project.locators.locators import LocatorAccountSettings
from auction_project.locators.locators_auction_events import LocatorAuctionEventsPage

from selenium import webdriver


class AuctionEventsPage(BasePage):
    pass


if __name__ == "__main__":
    # driver = webdriver.Chrome()
    # auc_ev = AuctionEventsPage(driver)
    #
    # account_settings_page = auc_ev.login_user(BASE_URL)
    # if account_settings_page:
    #     print("Account Settings page is found. Contact Preferences is displayed")
    #
    # cancel_bottom_button = auc_ev.wait_element(LocatorAccountSettings.CANCEL_BOTTOM_BUTTON)
    # cancel_bottom_button.click()
    #
    # h1_auction_events = auc_ev.wait_element(LocatorAuctionEventsPage.H1_AUCTION_EVENTS)
    # print(h1_auction_events)

    # calendar = auc_ev.wait_element(LocatorAuctionEventsPage.CALENDAR, timeout=15)
    # if calendar:
    #     print("Calendar is found")

    # calendar_shadow_root = auc_ev.wait_element(LocatorAuctionEventsPage.CALENDAR, timeout=15).shadow_root
    # calendar_shadow_text = calendar_shadow_root.find_element(*LocatorAuctionEventsPage.CALENDAR_SHADOW_VALUE).text
    # print(calendar_shadow_text)   # 02/16/2025

    today_date = date.today().strftime("%m/%d/%Y") # 02/16/2025
    print("Today's date:", today_date)
