import csv

from models.stock import StockModel


def build_response(data):
    times_series = data.get('Time Series (Daily)', None)
    if times_series:
        iterator = iter(times_series.items())
        last_info = next(iterator)[1]
        two_days_info = next(iterator)[1]
        last_close = float(last_info.get("4. close", 0))
        two_days_close = float(two_days_info.get("4. close", 0))

        variation = last_close - two_days_close
        stock = StockModel(
            open_price=last_info.get("1. open", 0),
            higher_price=last_info.get("2. high", 0),
            lower_price=last_info.get("3. low", 0),
            variation=variation
        )

        return stock
    return None


def build_symbols(data):
    cr = csv.reader(data.splitlines(), delimiter=',')
    my_list = list(cr)
    symbols = [row[0] for row in my_list]
    return symbols
