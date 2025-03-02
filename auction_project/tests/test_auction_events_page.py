import time

import pytest
from datetime import date
from selenium import webdriver

from auction_project.utility.date_calendar import Calendar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from auction_project.pages.auction_events_page import AuctionEventsPage
from auction_project.locators.locators_auction_events import LocatorAuctionEventsPage


@pytest.mark.usefixtures("driver", "login_user", 'wait_click_account_settings_cancel_button')
class TestAuctionEventsPage:
    def setup_method(self):
        self.auction_events = AuctionEventsPage(self.driver)

    # def test_0004_check_today_date_selected_calendar(self, driver, login_user,
    # wait_click_account_settings_cancel_button):
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

    # def test_0005_check_events_shown_in_schedule(self, driver, login_user, wait_click_account_settings_cancel_button):
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

    # def test_0006_check_today_elements_in_calendar_and_picker(self, driver, login_user,
    # wait_click_account_settings_cancel_button):
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
        # 3 different approaches to use utility functions:
        # 1. Initialise class as separate variable:
        #   calendar = Calendar()
        #   calendar.get_date_in_format(next_day_calc)
        # 2. Use @staticmentod in Class mentrods:
        # Example:
        # class Calendar:
        #    @staticmethod
        #    def get_date_in_format(self, date):
        #        # implementation of fuctions
        # example of usage:
        # Calendar.get_date_in_format(next_day_calc) #Calendar with no brackets "()"
        # 3. No class Calendar
        # Create functions like get_next_date without class in file date_calendar.py
        # Usage:
        # from ..date_calendar.py import get_next_date
        # get_next_date(today_date, number)
        next_day_calc = Calendar().get_next_date(today_date, number)
        next_day_calc_in_format = Calendar().get_date_in_format(next_day_calc)
        assert next_date_in_calendar == next_day_calc_in_format

    # def test_0007_check_calendar_pagination(self, driver, login_user, wait_click_account_settings_cancel_button):
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
        # alternative approach:
        assert self.auction_events.is_expected_date_as_short_weekday_date_in_events_block(
            yesterday_date, -6), "Mismatch between previous dates"

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
    # def test_0008_check_calendar_today_button_behavior(self, driver, login_user,
    # wait_click_account_settings_cancel_button):
    def test_0008_check_calendar_today_button_behavior(self):
        """Check calendars 'Today' button behavior"""
        # 1	Open Auction Events page
        h1_auction_events = self.auction_events.wait_element(LocatorAuctionEventsPage.H1_AUCTION_EVENTS)
        assert h1_auction_events.is_displayed(), "'Auction Events' page is not opened. H1 is not found"

        # 2 Check 'Today' button
        # 'Today' button is present
        # 'Today' button is not enabled
        today_button_disabled = self.auction_events.wait_element(LocatorAuctionEventsPage.TODAY_BUTTON_DISABLED)
        assert today_button_disabled.is_displayed(), "The 'Today' button is not displayed"
        assert today_button_disabled.is_enabled(), "The 'Today' button is enabled"

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
        today_button = self.auction_events.wait_element(LocatorAuctionEventsPage.TODAY_BUTTON_ENABLED)
        assert today_button.is_enabled(), "The 'Today' button is not enabled"

        # 6	Click on 'Today' button, check the button is not enabled
        today_button.click()

        today_button_disabled = self.auction_events.wait_element(LocatorAuctionEventsPage.TODAY_BUTTON_DISABLED)
        assert today_button_disabled.is_enabled(), "The 'Today' button is enabled"

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

        today_button_disabled = self.auction_events.wait_element(LocatorAuctionEventsPage.TODAY_BUTTON_DISABLED)
        assert today_button_disabled.is_enabled(), "The 'Today' button is enabled"

    def test_0009_01_check_6_days_blocks_shown_with_no_events_day(self):
        """Check that if no events scheduled, a text is shown.
        ** Current behavior of Auction Events page, that only 6 days are shown by default
    This test case should also predict case if not a single of 6 shown days has 'No Events Today' text"""
        # 1	Open Auction Events page
        h1_auction_events = self.auction_events.wait_element(LocatorAuctionEventsPage.H1_AUCTION_EVENTS)
        assert h1_auction_events.is_displayed(), "'Auction Events' page is not opened. H1 is not found"

        days_events_block = self.auction_events.wait_all_elements(LocatorAuctionEventsPage.DAY_BLOCKS)  # ERROR
        time.sleep(3)
        assert len(days_events_block) == 6, (f"Mismatch between the expected number of days. "
                                             f"Expected 6. Got {len(days_events_block)} number")

    @pytest.mark.xfail(reason='.NoSuchElementException: event_num_elem = day_block.find_element('
                              '*LocatorAuctionEventsPage.AUCTION_NUMBER).text.strip()')
    def test_0009_02_check_no_events_day(self):
        """Check that if no events scheduled, a text is shown.
                ** Current behavior of Auction Events page, that only 6 days are shown by default
            This test case should also predict case if not a single of 6 shown days has 'No Events Today' text"""
        # 1	Open Auction Events page
        h1_auction_events = self.auction_events.wait_element(LocatorAuctionEventsPage.H1_AUCTION_EVENTS)
        assert h1_auction_events.is_displayed(), "'Auction Events' page is not opened. H1 is not found"

        checkbox_limit_my_auctions = self.auction_events.wait_element(
            LocatorAuctionEventsPage.CHECKBOX_LIMIT_MY_AUCTIONS)
        assert checkbox_limit_my_auctions.is_displayed(), "The checkbox 'Limit to My Auctions' is not dispalyed"
        checkbox_limit_my_auctions.click()

        no_events_text = LocatorAuctionEventsPage.NO_EVENTS_TEXT
        no_events_in_block = self.auction_events.go_throw_events_lists_and_get_no_events_string()
        assert no_events_in_block == no_events_text

    # @pytest.mark.skip(reason="In work")
    def test_0009_03_check_no_events_day(self):
        """Check that if no events scheduled, a text is shown.
                ** Current behavior of Auction Events page, that only 6 days are shown by default
            This test case should also predict case if not a single of 6 shown days has 'No Events Today' text"""
        h1_auction_events = self.auction_events.wait_element(LocatorAuctionEventsPage.H1_AUCTION_EVENTS)
        assert h1_auction_events.is_displayed(), "'Auction Events' page is not opened. H1 is not found"

        checkbox_limit_my_auctions = self.auction_events.wait_element(
            LocatorAuctionEventsPage.CHECKBOX_LIMIT_MY_AUCTIONS)
        assert checkbox_limit_my_auctions.is_displayed(), "The checkbox 'Limit to My Auctions' is not dispalyed"
        checkbox_limit_my_auctions.click()

        no_events_text = "No Events Today"
        no_events = False
        while not no_events:
            days_events_list = []
            days_blocks = self.auction_events.wait_all_elements(LocatorAuctionEventsPage.DAY_BLOCKS)
            for block in days_blocks:
                assert block.is_displayed(), f"BLock {block} is not displayed"

                title_elem = WebDriverWait(block, 10).until(
                    EC.presence_of_element_located(LocatorAuctionEventsPage.AUCTION_DAY_H2)
                )
                assert title_elem.is_displayed(), f"Title element is not found for  {block}"
                title = title_elem.text.strip()

                events_elem = WebDriverWait(block, 10).until(
                    EC.presence_of_element_located(LocatorAuctionEventsPage.CONTENT_EVENTS_WITH_CHECKBOX)
                )
                assert events_elem.is_displayed(), f"No events found for {block}"
                events_value = events_elem.text.strip()
                norm_events_value = self.auction_events.normalize_text_without_n(events_value)

                day_dict = {title: norm_events_value}
                days_events_list.append(day_dict)

            print(days_events_list)

            for day in days_events_list:
                for event in day.values():
                    if event == no_events_text:
                        no_events = True
                        assert event == "No Events Today"
                        break
                    else:
                        # del days_events_list
                        right_arrow = self.auction_events.find_right_arrow()
                        right_arrow.click()

    @pytest.mark.skip(reason="In work. TimeoutException")
    def test_0006_02_check_user_can_select_date_in_calendar(self):
        """Check schedule is changed when calendar date is chosen.
        Verify that date selection in calendar works correctly."""

        # 1 Open Auction Events page
        h1_auction_events = self.auction_events.wait_element(LocatorAuctionEventsPage.H1_AUCTION_EVENTS)
        assert h1_auction_events.is_displayed(), "'Auction Events' page is not opened. H1 is not found"

        # 3 Get current date
        today_date = Calendar().get_today_date_without_format()
        # today_button_disabled = self.auction_events.wait_element(LocatorAuctionEventsPage.TODAY_BUTTON_DISABLED)
        days_numbers = [1, -1, 10, -10, 30, -30, 365, -365]

        for number in days_numbers:
            next_date_in_calendar = self.auction_events.select_target_day_number_in_calendar_picker(today_date, number)
            next_day_calc = Calendar().get_next_date(today_date, number)
            next_day_calc_in_format = Calendar().get_date_in_format(next_day_calc)

            assert next_date_in_calendar == next_day_calc_in_format, \
                f"Expected: {next_day_calc_in_format}, Got: {next_date_in_calendar}"

            today_button_enabled = self.auction_events.wait_element(LocatorAuctionEventsPage.TODAY_BUTTON_ENABLED)
            today_button_enabled.click()
            time.sleep(2)

