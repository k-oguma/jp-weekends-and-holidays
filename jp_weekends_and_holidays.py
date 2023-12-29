import argparse
import pandas as pd
import numpy as np
import holidays
import calendar

def get_holidays_and_weekends(year, month):
    jp_holidays = holidays.Japan(years=year)

    # 月末の日付を取得します
    last_day = calendar.monthrange(year, month)[1]

    # 土日と祝日を結合します
    weekends_and_holidays = [day for day in pd.date_range(start=f"{year}-{month}-01", end=f"{year}-{month}-{last_day}") if day.weekday() >= 5 or day.date() in jp_holidays]

    return weekends_and_holidays

def main():
    parser = argparse.ArgumentParser(description='Get weekends and holidays for a specific year and month.')
    parser.add_argument('year', type=int, help='The year to consider.')
    parser.add_argument('month', type=int, help='The month to consider.')
    args = parser.parse_args()

    # 日付のみ出力します
    for date in get_holidays_and_weekends(args.year, args.month):
        print(date.date())

if __name__ == "__main__":
    main()

