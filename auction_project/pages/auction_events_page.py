import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from datetime import date, timedelta
import datetime

from auction_project.pages.base_page import BasePage
from auction_project.creds import BASE_URL
from auction_project.locators.locators import LocatorAccountSettings
from auction_project.locators.locators_auction_events import LocatorAuctionEventsPage
from auction_project.utility.date_calendar import Calendar

from selenium import webdriver


class AuctionEventsPage(BasePage):

    def get_no_events_text(self, block):
        """Get day`s value in block events and normalize text.
        :return: string, 'No Events Today'"""
        no_events_text = WebDriverWait(block, timeout=10).until(
            EC.presence_of_element_located(LocatorAuctionEventsPage.AUCTION_NO_EVENTS)).text
        normalized_text = self.normalize_text(no_events_text)
        return normalized_text

    # 1
    def get_days_numbers_events(self):
        """Get days with numbers events in day in block events.
        Numbers of events are shown after clicking the checkbox "Limit to My Auctions".
        :return: list of dict{str: int},
        [{"Sun 3/2": "No Events Today"}, {"Mon 3/3": 7}, {"Tue 3/4": 19},
        {"Wed 3/5": 29}, {"Thu 3/6": 22}, {"Fri 3/7": 15}]"""
        list_events_per_day = []
        day_blocks = self.wait_all_elements(LocatorAuctionEventsPage.DAY_BLOCKS)

        for day_block in day_blocks:
            day_title = day_block.find_element(*LocatorAuctionEventsPage.AUCTION_DAY_H2).text.strip()
            try:
                events_number = WebDriverWait(day_block, timeout=15).until(
                    EC.presence_of_element_located(LocatorAuctionEventsPage.AUCTION_NUMBER)).text
                count_events = {day_title: int(events_number)}
                list_events_per_day.append(count_events)
            except:
                normalized_text = self.get_no_events_text(day_block)
                count_events = {day_title: normalized_text}
                list_events_per_day.append(count_events)

        return list_events_per_day

    def get_day_len_events_list(self):
        """Get number of events lists as length in block days events.
        :return: list of dict{str: int},
        [{"Sun 3/2": "No Events Today"}, {"Mon 3/3": 7}, {"Tue 3/4": 19},
        {"Wed 3/5": 29}, {"Thu 3/6": 22}, {"Fri 3/7": 15}]"""
        list_events_per_day = []
        day_blocks = self.wait_all_elements(LocatorAuctionEventsPage.DAY_BLOCKS)

        for day_block in day_blocks:
            day_title = day_block.find_element(*LocatorAuctionEventsPage.AUCTION_DAY_H2).text.strip()
            try:
                events_block = WebDriverWait(day_block, timeout=15).until(
                    EC.presence_of_all_elements_located(LocatorAuctionEventsPage.AUCTION_DAY_LI))
                count_events = {day_title: len(events_block)}
                list_events_per_day.append(count_events)
            except:
                normalized_text = self.get_no_events_text(day_block)
                count_events = {day_title: normalized_text}
                list_events_per_day.append(count_events)

        return list_events_per_day

    def get_expected_calendar_picker_header(self, date_without_format):
        """Get date and modify it to string.
        :return: string, 'March 2025'"""
        date_items_list = Calendar().get_date_items_list(date_without_format)
        expected_header_text = date_items_list[1] + ' ' + str(date_items_list[2])
        return expected_header_text

    def select_target_day_number_in_calendar_picker(self, current_day_without_format, number):
        """Get current date and calculate next date.
        Find the calendar picker and get a current text in the header.
        Construct the next date header as expected.
        Click on an arrow while the expected header will be shown.
        Click on target day in the picker.
        Get the expected date in the calendar date field.
        :return: string, '03/03/2025'"""
        picker_arrow = ''
        current_day_items_list = Calendar().get_date_items_list(current_day_without_format)
        current_month = current_day_items_list[1]
        current_year = current_day_items_list[2]

        target_day = Calendar().get_next_date(current_day_without_format, number)
        target_day_items_list = Calendar().get_date_items_list(target_day)
        target_day_number = target_day_items_list[0]
        target_month = target_day_items_list[1]
        target_year = target_day_items_list[2]
        target_day_xpath = f"//div[@class='v-btn__content'][contains(text(), '{target_day_number}')]"

        calendar_picker_header_element = self.wait_element(LocatorAuctionEventsPage.CALENDAR_PICKER_HEADER)
        calendar_picker_header = calendar_picker_header_element.text
        expected_header = f"{target_month} {target_year}"

        if current_month == target_month and current_year == target_year:
            target_day_element = self.wait_element((By.XPATH, target_day_xpath))
            target_day_element.click()

        else:
            if number > 0 and current_month != target_month or current_year != target_year:
                picker_arrow = LocatorAuctionEventsPage.RIGHT_PICKER_ARROW

            elif number < 0 and current_month != target_month or current_year != target_year:
                picker_arrow = LocatorAuctionEventsPage.LEFT_PICKER_ARROW

            count = 0
            while calendar_picker_header != expected_header:
                arrow = self.wait_element(picker_arrow)
                arrow.click()
                count += 1
                time.sleep(1)  # Give time to calendar to update
                calendar_picker_header = self.wait_element(LocatorAuctionEventsPage.CALENDAR_PICKER_HEADER).text

            target_day_element = self.wait_element((By.XPATH, target_day_xpath))
            target_day_element.click()

        calendar_value = self.get_shadow_root_value(
            LocatorAuctionEventsPage.CALENDAR, LocatorAuctionEventsPage.CALENDAR_SHADOW_VALUE)

        return calendar_value

    def find_right_arrow(self):
        """Find all right arrows. Set the right arrow"""
        right_arrows = self.wait_all_elements(LocatorAuctionEventsPage.RIGHT_EVENTS_BLOCK_ARROWS)
        right_arrow = right_arrows[5]
        return right_arrow

    def find_left_arrow(self):
        """Find all left arrows. Set the left arrow"""
        left_arrows = self.wait_all_elements(LocatorAuctionEventsPage.LEFT_EVENTS_BLOCK_ARROWS)
        left_arrow = left_arrows[0]
        return left_arrow

    def get_next_date_and_calculate_expected_date(self, yesterday_date, number):
        """Get list dates of events block.
        Calculate next expected date. Modify the date view as short.
        :return: date, 'Sun 3/2'."""
        next_dates = self.wait_all_elements(LocatorAuctionEventsPage.LIST_BLOCK_DATES)
        nx_dts = []
        for dt in next_dates:
            nx_dts.append(dt.text)

        expected_next_date = Calendar().get_next_date(yesterday_date, number)
        exp_short_nx_date = Calendar().get_short_weekday_date_in_events_block(expected_next_date)
        next_date_in_week_block = nx_dts[0]
        return next_date_in_week_block, exp_short_nx_date


if __name__ == "__main__":
    driver = webdriver.Chrome()
    auc_ev = AuctionEventsPage(driver)

    account_settings_page = auc_ev.login_user(BASE_URL)
    if account_settings_page:
        print("Account Settings page is found. Contact Preferences is displayed")

    cancel_bottom_button = auc_ev.wait_element(LocatorAccountSettings.CANCEL_BOTTOM_BUTTON)
    cancel_bottom_button.click()

    h1_auction_events = auc_ev.wait_element(LocatorAuctionEventsPage.H1_AUCTION_EVENTS).text
    print(f"Title '{h1_auction_events}' is found")

    # --------- 0004
    calendar = auc_ev.wait_element(LocatorAuctionEventsPage.CALENDAR, timeout=15)
    if calendar:
        print("Calendar is found")

    # calendar_shadow_root = auc_ev.wait_element(LocatorAuctionEventsPage.CALENDAR, timeout=15).shadow_root
    # calendar_shadow_text = calendar_shadow_root.find_element(*LocatorAuctionEventsPage.CALENDAR_SHADOW_VALUE).text
    # print(calendar_shadow_text)   # 02/16/2025

    # ---- 0004
    # today = date.today().strftime("%m/%d/%Y")  # 02/16/2025
    # today = datetime.datetime.today().strftime("%m/%d/%Y")
    # print("Today's date:", today)
    #
    # today_dt = datetime.datetime.now()
    # print("Today's day", today_dt, today_dt.day)
    # # next_day = today + timedelta

    # ----0005
    # list_events = auc_ev.get_day_len_events_list()
    # print(list_events)

    # checkbox_limit = auc_ev.search_element(LocatorAuctionEventsPage.CHECKBOX_LIMIT_MY_AUCTIONS)
    # checkbox_limit.click()
    #
    # list_numbers = auc_ev.get_days_numbers_events()
    # print(list_numbers)

    # blocks_with_count = auc_ev.wait_all_elements(LocatorAuctionEventsPage.AUCTION_COUNT)
    # for block in blocks_with_count:
    #     print(block.text)
    # print(len(blocks_with_count))

    # days_titles = auc_ev.wait_all_elements(LocatorAuctionEventsPage.AUCTION_DAY_H2)
    # if days_titles:
    #     print("H2 titles are found", len(days_titles))
    #
    # li_elements = auc_ev.wait_all_elements(LocatorAuctionEventsPage.AUCTION_DAY_LI)
    # if li_elements:
    #     print("Events lists are found", len(li_elements))

    # ---0006 select date

    # 0.получить сегодняшний день
    #         # - дату, месяц, год
    today_date = Calendar().get_today_date_without_format()
    exp_header = auc_ev.get_expected_calendar_picker_header(today_date)
    # print(exp_header)

    # 4. Вычислить дату следующего дня
    # tomorrow_date = Calendar().get_next_date(today_date, 1)
    # print(tomorrow_date)  # 2025-02-21 16:25:54.856285
    # exp_header_tomorrow = auc_ev.get_expected_calendar_picker_header(tomorrow_date)
    # print("Exp tom header: ", exp_header_tomorrow)

    calendar.click()
    calendar_picker = auc_ev.search_element(LocatorAuctionEventsPage.CALENDAR_PICKER)
    # if calendar_picker:
    #     print("Picker found")

    calendar_field_value_text = auc_ev.select_target_day_number_in_calendar_picker(today_date, 10)
    print("calendar field value text", calendar_field_value_text)
