import time

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

        checkbox_limit = self.auction_events.search_element(LocatorAuctionEventsPage.CHECKBOX_LIMIT_MY_AUCTIONS)
        checkbox_limit.click()

        numbers_events = self.auction_events.get_days_numbers_events()

        assert len_events_in_days == numbers_events, \
            f"Mismatch between the list of events in the schedule and the number of events! "
        f"Expected: {len_events_in_days}, but got: {numbers_events}"

    def test_0006_check_today_elements_in_calendar_and_picker(self):
        """ Verify that date selection in calendar works correctly.
        Verify that items of current date in calendar and picker work correctly."""

        # 1 Open Auction Events page
        h1_auction_events = self.auction_events.wait_element(LocatorAuctionEventsPage.H1_AUCTION_EVENTS)
        assert h1_auction_events.is_displayed(), "'Auction Events' page is not opened. H1 is not found"

        # 2 Click on date. Calendar popup opened
        calendar_element = self.auction_events.wait_element(LocatorAuctionEventsPage.CALENDAR)
        calendar_element.click()

        calendar_picker = self.auction_events.search_element(LocatorAuctionEventsPage.CALENDAR_PICKER)
        assert calendar_picker.is_displayed(), "Calendar picker is not displayed"

        # 3 Get current date: day, month, year
        today_date = Calendar().get_today_date_without_format()

        # 4 Check text in the calendar picker header, current day
        expected_header_picker_text = self.auction_events.get_expected_calendar_picker_header(today_date)
        calendar_picker_header = self.auction_events.search_element(
            LocatorAuctionEventsPage.CALENDAR_PICKER_HEADER).text
        assert calendar_picker_header == expected_header_picker_text, "Calendar header is not as expected header"

        # 5 Check active day in picker
        active_day_in_picker = self.auction_events.search_element(LocatorAuctionEventsPage.ACTIVE_DAY_PICKER)
        assert active_day_in_picker.is_displayed(), "Active button of today`s day is not shown"

        expected_today_day_number = Calendar().get_day_number(today_date)
        active_today_day_number_in_picker = active_day_in_picker.text
        assert active_today_day_number_in_picker == str(expected_today_day_number)

        # 5. Calculate next date, select next date, check displaying next date in format in the calendar field
        number = 60
        next_date_in_calendar = self.auction_events.select_target_day_number_in_calendar_picker(today_date, number)
        next_day_calc = Calendar().get_next_date(today_date, number)
        next_day_calc_in_format = Calendar().get_date_in_format(next_day_calc)
        assert next_date_in_calendar == next_day_calc_in_format

    def test_0007_check_calendar_pagination(self):
        """Check date is changed page by one week, when pressing on < or > button"""

        # 1	Open Auction Events page
        h1_auction_events = self.auction_events.wait_element(LocatorAuctionEventsPage.H1_AUCTION_EVENTS)
        assert h1_auction_events.is_displayed(), "'Auction Events' page is not opened. H1 is not found"

        # 2	Check < and > change page button are present
        # < and > change page button are present
        # < and > change page button are enabled
        right_arrow = self.auction_events.find_right_arrow()
        assert right_arrow.is_displayed(), "Right events block arrow is not displayed"
        assert right_arrow.is_enabled(), "Right events block arrow is not enabled"

        left_arrow = self.auction_events.find_left_arrow()
        assert left_arrow.is_displayed(), "Left events block arrow is not displayed"
        assert left_arrow.is_enabled(), "Left events block arrow is not enabled"

        # 3 Click on < button, Scheduler changed exact one week (6 days ago) previous current week
        week_dates = self.auction_events.wait_all_elements(LocatorAuctionEventsPage.LIST_BLOCK_DATES)
        yesterday_date_block = week_dates[0].text

        # -- Calculate dates: today, yesterday
        today_date = Calendar().get_today_date_without_format()
        yesterday_date = Calendar().get_next_date(today_date, -1)
        yesterday_short_date = Calendar().get_short_weekday_date_in_events_block(yesterday_date)
        assert yesterday_date_block == yesterday_short_date, "Mismatch between yesterday dates"

        # -- Click on < left arrow, check date - (-6 days)
        left_arrow.click()
        previous_date_in_week, exp_short_prev_date = self.auction_events.get_next_date_and_calculate_expected_date(
            yesterday_date, -6)
        assert previous_date_in_week == exp_short_prev_date, "Mismatch between previous dates"

        # 4 Click on > button, Scheduler changed exact one week forward current week
        # -- return to the current week
        right_arrow = self.auction_events.find_right_arrow()
        right_arrow.click()
        time.sleep(1)
        assert yesterday_date_block == yesterday_short_date, "Mismatch between yesterday dates"

        # click on > button, to the future week
        right_arrow = self.auction_events.find_right_arrow()
        right_arrow.click()
        time.sleep(1)

        future_date_in_week, exp_short_future_date = self.auction_events.get_next_date_and_calculate_expected_date(
            yesterday_date, 6)
        assert future_date_in_week == exp_short_future_date, "Mismatch between future dates"

    @pytest.mark.xfail(reason="assert not today_button.is_enabled(). AssertionError"
                              "The button is enabled and clickable after opening the page in Chrome."
                              "Working as designed")
    def test_0008_check_calendar_today_button_behavior(self):
        """Check calendars 'Today' button behavior"""
        # 1	Open Auction Events page
        h1_auction_events = self.auction_events.wait_element(LocatorAuctionEventsPage.H1_AUCTION_EVENTS)
        assert h1_auction_events.is_displayed(), "'Auction Events' page is not opened. H1 is not found"

        # 2 Check 'Today' button
        # 'Today' button is present
        # 'Today' button is not enabled
        today_button = self.auction_events.wait_element(LocatorAuctionEventsPage.TODAY_BUTTON)
        # assert today_button.is_displayed(), "The 'Today' button is not displayed"
        assert not today_button.is_enabled(), "The 'Today' button is enabled"  # ! ERROR

        # 3	Click on date, Calendar popup opened
        calendar = self.auction_events.wait_element(LocatorAuctionEventsPage.CALENDAR)
        calendar.click()
        picker = self.auction_events.wait_element(LocatorAuctionEventsPage.CALENDAR_PICKER)
        assert picker.is_displayed(), "The calendar picker is not displayed"
        today_date = Calendar().get_today_date_without_format()

        # 4	Choose any date and click on it. Check next date is shown in the date field
        next_date = self.auction_events.select_target_day_number_in_calendar_picker(today_date, 2)
        calendar_value = self.auction_events.get_shadow_root_value(
            LocatorAuctionEventsPage.CALENDAR, LocatorAuctionEventsPage.CALENDAR_SHADOW_VALUE)
        assert calendar_value == next_date

        # 5	Check 'Today' button enables
        assert today_button.is_enabled(), "The 'Today' button is not enabled"

        # 6	Click on 'Today' button, check the button is not enabled
        today_button.click()
        assert not today_button.is_enabled(), "The 'Today' button is enabled"  # ! ERROR
        # assert today_button.is_enabled()

        # 7	Click on > button
        right_arrow = self.auction_events.find_right_arrow()
        assert right_arrow.is_displayed(), "Right events block arrow is not displayed"
        assert right_arrow.is_enabled(), "Right events block arrow is not enabled"
        right_arrow.click()

        # 8	Click on < button
        left_arrow = self.auction_events.find_left_arrow()
        assert left_arrow.is_displayed(), "Left events block arrow is not displayed"
        assert left_arrow.is_enabled(), "Left events block arrow is not enabled"
        left_arrow.click()

    @pytest.mark.skip(reason="for, ElementNotInteractableException")
    def test_0006_02_check_user_can_select_date_in_calendar(self):
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

        # 3 Get current date
        today_date = Calendar().get_today_date_without_format()

        days_numbers = [1, -1, 10, -10, 30, -30, 365, -365]
        for number in days_numbers:
            next_date_in_calendar = self.auction_events.select_target_day_number_in_calendar_picker(today_date, number)
            next_day_calc = Calendar().get_next_date(today_date, number)
            next_day_calc_in_format = Calendar().get_date_in_format(next_day_calc)

            assert next_date_in_calendar == next_day_calc_in_format, \
                f"Expected: {next_day_calc_in_format}, Got: {next_date_in_calendar}"

        # # Возвращаемся к сегодняшней дате и проверяем
        # today_date_in_calendar = self.auction_events.select_target_day_number_in_calendar_picker(today_date, 0)
        # today_date_in_format = Calendar().get_date_in_format(today_date)
        # assert today_date_in_calendar == today_date_in_format, \
        #     f"Expected: {today_date_in_format}, Got: {today_date_in_calendar}"
