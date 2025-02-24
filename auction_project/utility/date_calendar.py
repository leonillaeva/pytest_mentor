# import datetime


from datetime import datetime, timedelta


class Calendar:
    def get_today_date_without_format(self):
        """Get current date.
        :return: <class 'datetime.datetime'>
        2025-02-20 15:40:32.233772"""
        today_date_without_format = datetime.today()
        return today_date_without_format

    def get_date_in_format(self, date):
        """Convert date in format.
        :return: <class 'str'>
        02/20/2025"""
        return date.strftime("%m/%d/%Y")

    def get_day_number(self, date):
        """Get day number.
        :return: <class 'int'>, 21"""
        day_number = date.day
        return day_number

    def get_name_month(self, date):
        """Get name of month.
        :return: <class 'str'>, February"""
        name_month = date.strftime("%B")
        return name_month

    def get_year(self, date):
        """Get number of year.
        :return: <class 'int'>, 2025"""
        return date.year

    def get_next_date(self, today_date, number):
        """Calculate next date from current date.
        : return: <class 'datetime.datetime'>
        2025-02-21 15:44:36.682587"""
        next_date = today_date + timedelta(days=number)
        return next_date

    def get_date_items_list(self, date_without_format):
        """Get a day, month string, year in the list.
        :return: list[int, str, int],
        [20, 'February', 2025]"""
        day = Calendar().get_day_number(date_without_format)
        month = Calendar().get_name_month(date_without_format)
        year = Calendar().get_year(date_without_format)
        date_items_list = [day, month, year]
        return date_items_list

    def get_weekday(self, date_without_format):
        """Get a weekday, short version
        :return: <class 'str'>, -> Wed"""
        return date_without_format.strftime("%a")

    def get_short_weekday_date_in_events_block(self, date_without_format):
        """Construct and get short weekday.
        :return: string, 'Tue 2/25'"""
        weekday_short = self.get_weekday(date_without_format)
        month = date_without_format.month
        day = date_without_format.day
        date = f"{month}/{day}"
        return f"{weekday_short} {date}"


if __name__ == "__main__":
    # --------0006 select date
    calendar = Calendar()
    today_without_format = calendar.get_today_date_without_format()
    # print(f"Today without format: {today_without_format}")


    # print(today_without_format.strftime("%A"))
    # print(today_without_format.strftime("%a"))
    # today_in_format = calendar.get_date_in_format(today_without_format)
    # today_day = calendar.get_day_number(today_without_format)
    # print(f"Today day: {today_day}")
    #
    # # print(f"Today: {today_without_format}, in format: {today_in_format}")
    # # print(type(today_without_format))
    # # print(type(today_in_format))
    # # print("Today's list", calendar.get_date_items_list(today_without_format))
    # #
    # tomorrow_date = calendar.get_next_date(today_without_format, 1)
    # # print(f"Tomorrow: {tomorrow}")
    # tomorrow_day_number = calendar.get_day_number(tomorrow_date)
    # # print("Day tomorrow: ", tomorrow_day_number)
    # # print(type(tomorrow_day_number))
    #
    # # print("Tomorrow`s list", calendar.get_date_items_list(tomorrow_date))
    # tomorrow_month = calendar.get_name_month(tomorrow_date)
    # # print(tomorrow_month)
    # # print(type(tomorrow_month))
    # tomorrow_year = calendar.get_year(tomorrow_date)
    # print(tomorrow_year)
    # print(type(tomorrow_year))
# -------------0007
    # today_weekday = calendar.get_weekday(today_without_format)
    # print(today_weekday)
    # print(type(today_weekday))
    today_short_date = calendar.get_short_weekday_date_in_events_block(today_without_format)
    print(today_short_date)

    yesterday = calendar.get_next_date(today_without_format, -1)
    print("Yesterday", yesterday)

    next_date_min = calendar.get_next_date(yesterday, -6)
    # print(next_date_min) # 2025-02-15 16:28:47.962448
    next_short_min = calendar.get_short_weekday_date_in_events_block(next_date_min)
    print("Expected", next_short_min) # Sat 02/15