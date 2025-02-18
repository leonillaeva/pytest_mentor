# import datetime


from datetime import datetime, timedelta


class Calendar:
    def get_today_date_without_format(self):
        today_date = datetime.today()
        return today_date

    def get_today_date_in_format(self, date):
        return date.strftime("%m/%d/%Y")

    def get_day_number(self, date):
        day_number = date.day
        return day_number

    def get_name_month(self, date):
        name_month = date.strftime("%B") # February
        return name_month

    def get_year(self, date):
        return date.year

    def get_next_date(self, today_date):
        tomorrow_date = today_date + timedelta(days=1)
        return tomorrow_date


if __name__ == "__main__":
    # --------0006 select date
    calendar = Calendar()
    today = calendar.get_today_date_without_format()
    today_in_format = calendar.get_today_date_in_format(today)

    #print(f"Today: {today}, in format: {today_in_format}")

    tomorrow = calendar.get_next_date(today)
    # print(f"Tomorrow: {tomorrow}")
    tomorrow_day_number = calendar.get_day_number(tomorrow)
    print("Day tomorrow: ", tomorrow_day_number)
    tomorrow_month = calendar.get_name_month(tomorrow)
    tom_year = calendar.get_year(tomorrow)
    print(tomorrow_month, tom_year)

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
