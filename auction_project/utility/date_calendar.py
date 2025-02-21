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


if __name__ == "__main__":
    # --------0006 select date
    calendar = Calendar()
    today_without_format = calendar.get_today_date_without_format()
    today_in_format = calendar.get_date_in_format(today_without_format)
    today_day = calendar.get_day_number(today_without_format)
    # print(f"Today day: {today_day}")

    # print(f"Today: {today_without_format}, in format: {today_in_format}")
    # print(type(today_without_format))
    # print(type(today_in_format))
    # print("Today's list", calendar.get_date_items_list(today_without_format))
    #
    tomorrow_date = calendar.get_next_date(today_without_format, 1)
    # print(f"Tomorrow: {tomorrow}")
    tomorrow_day_number = calendar.get_day_number(tomorrow_date)
    # print("Day tomorrow: ", tomorrow_day_number)
    # print(type(tomorrow_day_number))

    # print("Tomorrow`s list", calendar.get_date_items_list(tomorrow_date))
    tomorrow_month = calendar.get_name_month(tomorrow_date)
    # print(tomorrow_month)
    # print(type(tomorrow_month))
    tomorrow_year = calendar.get_year(tomorrow_date)
    print(tomorrow_year)
    print(type(tomorrow_year))

    # -----------------след день 0006
    # 1. Кликнуть на календарь
    # 2. Проверить что появился пикер.
    #
    # 3 выбрать следующий день
    # 3.получить сегодняшний день
    # - дату, месяц, год
    #
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

    # ----------------------------
    # from datetime import datetime, timedelta
    #
    # # Using current time
    # ini_time_for_now = datetime.now()
    #
    # # printing initial_date
    # print(str(ini_time_for_now))
    #
    # # Calculating future dates
    # # for two years
    # future_date_after_2yrs = ini_time_for_now + timedelta(days=730)
    #
    # future_date_after_2days = ini_time_for_now + timedelta(days=2)
    #
    # # printing calculated future_dates
    # print('future_date_after_2yrs:', str(future_date_after_2yrs))
    # print('future_date_after_2days:', str(future_date_after_2days))
