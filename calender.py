# CALENDER SYSTEM
import calendar

months = {1: 0, 2: 3, 3: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5}
week_day = {0: 'SUNDAY', 1: 'MONDAY', 2: 'TUESDAY', 3: 'WEDNESDAY', 4: 'THURSDAY', 5: 'FRIDAY', 6: 'SATURDAY'}
data_list = []

if __name__ == "__main__":
    print("\t WHICH DAY OF THE WEEK LETS HAVE A TRY")
    while True:
        user_date, user_month, user_year = map(int, input("\nENTER  Any DATE MONTH YEAR like 10 07 1996: ").split())
        year_code = 0 if 1999 >= user_year >= 1900 else 6
        last_2_digit_year = user_year % 100
        data_list.extend((year_code, user_date, months[user_month], last_2_digit_year, last_2_digit_year // 4))
        week_code = sum(data_list) % 7
        print(week_day[week_code])
        print(calendar.month(user_year, user_month))
