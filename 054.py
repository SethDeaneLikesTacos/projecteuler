import resources.pef as pef
import time
"""
https://projecteuler.net/problem=54
"""


def hand_value(values, suits):
    """
    Given cards of a hand, the relative value of that
    hand will be returned
    """




def main():

    raw_list = open("resources/054.txt", "r").read()
    raw_lists = raw_list.split("\n")[0:-1]
    for l in raw_lists:
        hand_one = l[0:14]
        hand_one_values = hand_one[0:12:3]
        print(hand_one_values)
        # hand_one_suits = 

        # hand_two = l[15:]
        # hand_two_values = hand_two[]
        # hand_two_suits = 

        return 

main()

# if __name__ == "__main__":
#     start_time = time.time()
#     answer = main()
#     end_time = time.time()
#     pef.answer(answer, end_time - start_time)
