import collections
import numpy as np
import datetime


def calculate(data):
    total = 0
    total_vol = 0
    for price, vol in data:
        total_vol += vol
        total += price * vol
    return total / total_vol


def get_wk():
    stock = np.dtype([('name', np.str_, 2),
                      ('time', np.str_, 10),
                      ('open_price', np.float64),
                      ('close_price', np.float64),
                      ('low_price', np.float64),
                      ('high_price', np.float64),
                      ('volume', np.int32)])
    jd_stock = np.loadtxt('JD.csv', delimiter=',', dtype=stock)

    record = collections.defaultdict(list)
    # fetch the dict: (year, week number): [(close_price1, volume1),(close_price2, volume2)....]
    for stock_day in jd_stock:
        date = datetime.datetime.strptime(stock_day['time'], "%m/%d/%Y")
        year = int(date.strftime('%Y'))
        week = int(date.strftime('%U'))
        record[(year, week)].append((stock_day['close_price'], stock_day['volume']))
    # get the (year, week): average
    return {k: calculate(v) for k, v in record.items()}


def print_top_bottom_5(data):
    # sort the week data
    sort_data = sorted(data.items(), key=lambda x: x[0])
    # slice top 5 and bottom 5
    top_bottom = sort_data[:5] + sort_data[-5:]
    # Limit Floats to 3 Decimal
    print({k: round(v, 3) for k, v in dict(top_bottom).items()})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    week_data = get_wk()
    print_top_bottom_5(week_data)
