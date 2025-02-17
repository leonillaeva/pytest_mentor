import pytest
from datetime import date
from selenium import webdriver

from auction_project.creds import ACCOUNT_SETTINGS_URL
from auction_project.pages.auction_events_page import AuctionEventsPage
from auction_project.locators.locators import LocatorAccountSettings
from auction_project.locators.locators_auction_events import LocatorAuctionEventsPage


@pytest.mark.usefixtures("driver", "login_user", 'wait_click_account_settings_cancel_button')
class TestAuctionEventsPage:
    def setup_method(self):
        self.auction_events = AuctionEventsPage(self.driver)

    def test_0004_check_today_date_selected_calendar(self):
        """Test to check if today's date is selected by default in the calendar."""

        # 1 Open Auction Events page
        h1_auction_events = self.auction_events.wait_element(LocatorAuctionEventsPage.H1_AUCTION_EVENTS)
        assert h1_auction_events.is_displayed(), "'Auction Events' page is not opened. H1 is not found"

        # 2 Check that Date in calendar is set to today`s date
        calendar_value = self.auction_events.get_shadow_root_value(
            LocatorAuctionEventsPage.CALENDAR, LocatorAuctionEventsPage.CALENDAR_SHADOW_VALUE)
        # print(calendar_value)
        today_date = date.today().strftime("%m/%d/%Y")
        assert calendar_value == today_date, f"Calendar value is not matched, today`s date {today_date}"

