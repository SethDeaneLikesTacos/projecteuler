import resources.pef as pef
import time
from datetime import date, timedelta
"""
https://projecteuler.net/problem=19
0.03850817680358887
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
