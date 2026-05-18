from tornado.options import options

call_month_arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
put_month_arr = ["M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"]

def extract_data_from_ticker(ticker):

    month = ticker[7]
    year = ticker[8]
    week = ticker[9] if ticker[9] else 3 #month-option

    if month in call_month_arr:
        option_type = "CALL"
        month = call_month_arr.index(month) + 1
    elif month in put_month_arr:
        option_type = "PUT"
        month = put_month_arr.index(month) + 1