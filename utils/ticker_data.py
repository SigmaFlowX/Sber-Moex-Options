from datetime import datetime
import calendar

call_month_arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
put_month_arr = ["M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"]
week_arr = ["A", "B", "C", "D"]


def nth_weekday(year: int, month: int, weekday: int, n: int):
    weeks = calendar.monthcalendar(year, month)
    days = [week[weekday] for week in weeks if week[weekday] != 0]

    return days[n - 1]

def extract_data_from_ticker(ticker:str):

    month = ticker[6]
    year = ticker[7]
    week = week_arr.index(ticker[8]) + 1 if ticker[8] else 3 #month-option


    if month in call_month_arr:
        option_type = "CALL"
        month = call_month_arr.index(month) + 1
    elif month in put_month_arr:
        option_type = "PUT"
        month = put_month_arr.index(month) + 1



ticker = "SR330CQ6D"
extract_data_from_ticker(ticker)