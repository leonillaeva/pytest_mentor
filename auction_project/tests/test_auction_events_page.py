import pytest
from datetime import date
import datetime
from selenium import webdriver

from auction_project.utility.date_calendar import Calendar
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

    def test_0005_check_events_shown_in_schedule(self):
        """Verify Schedule show events"""
        # 1 Open Auction Events page
        h1_auction_events = self.auction_events.wait_element(LocatorAuctionEventsPage.H1_AUCTION_EVENTS)
        assert h1_auction_events.is_displayed(), "'Auction Events' page is not opened. H1 is not found"

        # 2 Check events are shown in scheduler
        len_events_in_days = self.auction_events.get_day_len_events_list()
        # print(len_events_in_days)

        checkbox_limit = self.auction_events.search_element(LocatorAuctionEventsPage.CHECKBOX_LIMIT_MY_AUCTIONS)
        checkbox_limit.click()

        numbers_events = self.auction_events.get_days_numbers_events()
        # print(numbers_events)

        assert len_events_in_days == numbers_events, \
            f"Mismatch between the list of events in the schedule and the number of events! "
        f"Expected: {len_events_in_days}, but got: {numbers_events}"

        # len_events_in_days_dict = {k: v for day in len_events_in_days for k, v in day.items()}
        # numbers_events_dict = {k: v for day in numbers_events for k, v in day.items()}

        # assert len_events_in_days_dict == numbers_events_dict, (
        #     f"Mismatch between the list of events in the schedule and the number of events! "
        #     f"Expected: {len_events_in_days_dict}, but got: {numbers_events_dict}")

    def test_0006_check_user_can_select_date_in_calendar(self):
        """Check schedule is changed when calendar date is chosen.
        Verify that date selection in calendar works correctly."""

        # 1 Open Auction Events page
        h1_auction_events = self.auction_events.wait_element(LocatorAuctionEventsPage.H1_AUCTION_EVENTS)
        assert h1_auction_events.is_displayed(), "'Auction Events' page is not opened. H1 is not found"

        # 2 Click on date. Calendar popup opened
        calendar_element = self.auction_events.wait_element(LocatorAuctionEventsPage.CALENDAR)
        calendar_element.click()

        calendar_picker = self.auction_events.search_element(LocatorAuctionEventsPage.CALENDAR_PICKER)
        assert calendar_picker.is_displayed(), "Calendar picker is not displayed"

        # 0.получить сегодняшний день
        #         # - дату, месяц, год
        today_date = Calendar().get_today_date_without_format()

        # 4. Вычислить дату следующего дня
        # 5. получить данные след дня
        # - дату, месяц, год
        tomorrow_date = Calendar().get_next_date(today_date)
        tomorrow_day_number = Calendar().get_day_number(tomorrow_date)
        tomorrow_month = Calendar().get_name_month(tomorrow_date)
        tomorrow_year = Calendar().get_year(tomorrow_date)

        # 6. Проверить месяц, год в пикере 'February 2025' - сложить как в пикере
        header_picker_text = str(tomorrow_month) + ' ' + str(tomorrow_year)
        print("+", header_picker_text)
        calendar_picker_header = self.auction_events.search_element(
            LocatorAuctionEventsPage.CALENDAR_PICKER_HEADER).text
        print("in calendar", calendar_picker_header)
        assert calendar_picker_header == header_picker_text

# -----------------след день 0006
# 0.получить сегодняшний день
#         # - дату, месяц, год
# 1. Кликнуть на календарь
# 2. Проверить что появился пикер.
#
# 3 - Выбрать следующий день
# 4. Вычислить дату следующего дня
#
# 5. получить данные след дня
# - дату, месяц, год
#
# 6. Проверить месяц, год в пикере - сложить как в пикере
# - проверить, если соответствует -> выбирать число даты
# если не соответствует, найти правую стрелку, кликнуть по ней
# Проверить месяц, год в пикере
# - проверить, если соответствует -> выбирать число даты
#  7. Проверить что дата отображается в поле календаря.
