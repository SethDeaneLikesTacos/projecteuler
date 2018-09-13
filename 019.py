import pef
import time
from datetime import date, timedelta
"""
You are given the following information, but you may prefer
to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but
  not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the
twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


startdate = date(1901 ,1, 1)
enddate   = date(2000 ,12, 31)

def main():

    total = 0

    # generate list of datetime object between start and end date
    dd = [startdate + timedelta(days=x) for x in range((enddate-startdate).days + 1)]
    for d in dd:
        if d.weekday() == 6 and d.day == 1:
            total += 1

    return total


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
