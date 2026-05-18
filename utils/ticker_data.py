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
    year = int(ticker[7]) + 2020
    week = week_arr.index(ticker[8]) + 1 if ticker[8] else 3 #month-option


    if month in call_month_arr:
        option_type = "CALL"
        month = call_month_arr.index(month) + 1
    elif month in put_month_arr:
        option_type = "PUT"
        month = put_month_arr.index(month) + 1
    else:
        raise ValueError("Could not determine the month")

    day = nth_weekday(year, month, calendar.WEDNESDAY, week)

    expiry_date = datetime(year, month, day)

    return option_type, expiry_date

def main():
    ticker = "SR330CQ6D"
    print(extract_data_from_ticker(ticker))

if __name__ == "__main__":
    main()