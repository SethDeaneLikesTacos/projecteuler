import resources.pef as pef
import time
"""
Starting in the top left corner of a 2×2 grid, and only
being able to move to the right and down, there are
exactly 6 routes to the bottom right corner.

tl : right, right, down,  down  : br
tl : right, down,  right, down  : br
tl : right, down,  down,  right : br
tl : down,  right, right, down  : br
tl : down,  right, down,  right : br
tl : down,  down,  right, right : br

How many such routes are there through a 20×20 grid?

SOLUTION:
     40! / (20! * 20!) = 137846528820
"""


def main():

    return 137846528820


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
