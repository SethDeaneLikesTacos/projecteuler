import resources.pef as pef
import time
from collections import Counter
"""
https://projecteuler.net/problem=54
0.15555572509765625
"""

card_dict = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
    'D': 'D',
    'S': 'S',
    'C': 'C',
    'H': 'H'}


def find_repeats(lst, val):
    """
    lst: list of numbers to search for pairs, trios, etc.
    val: 2 = pairs, 3 = trios, 4 = quads, etc.
    Return: list of groups that were of that size.
    """
    groups = []
    for k, v in Counter(lst).items():
        groups.extend([k] * (v // val))
    return groups


def parse_hand(hand, offset):
    """
    hand: string representation of a hand
    offset: 0 = value, 1 = suit
    Return: list of card values or suits
    """
    hand_vals_str = hand[offset:14:3]
    hand_vals = []
    for i in hand_vals_str:
        hand_vals.append(card_dict.get(i))

    return hand_vals


def high_card(hand):
    """ High Card: Highest value card. Returns highest card of hand. """
    hand_vals = parse_hand(hand, 0)

    return max(hand_vals)


def one_pair(hand):
    """ One Pair: Two cards of the same value. Returns highest pair of hand. If no pairs, returns 0. """
    hand_vals = parse_hand(hand, 0)
    pairs = find_repeats(hand_vals, 2)

    if len(pairs) != 1:
        return 0

    return max(pairs)


def two_pair(hand):
    """ Two Pairs: Two different pairs. Returns highest of both pairs for hand. If no 2 pairs, returns 0. """
    hand_vals = parse_hand(hand, 0)
    pairs = find_repeats(hand_vals, 2)

    if len(pairs) != 2:
        return 0

    return max(pairs)
    

def three_of_a_kind(hand):
    """ Three of a Kind: Three cards of the same value. Returns the value of the trio. If no trio, return 0. """
    hand_vals = parse_hand(hand, 0)
    trios = find_repeats(hand_vals, 3)

    if len(trios) == 0:
        return 0

    return max(trios)


def straight(hand):
    """ Straight: All cards are consecutive values. Return 1 if straight, otherwise 0. """
    hv = parse_hand(hand, 0)
    hv.sort()

    if hv[1] - hv[0] == 1 and hv[2] - hv[0] == 2 and hv[3] - hv[0] == 3 and hv[4] - hv[0] == 4:
        return 1
    
    return 0


def flush(hand):
    """ Flush: All cards of the same suit. Returns 1 if flush, otherwise 0. """
    hand_suits = hand[1:14:3]

    if hand_suits == len(hand_suits) * hand_suits[0]:
        return 1

    return 0


def full_house(hand):
    """ Full House: Three of a kind and a pair. Return 1 if full house, otherwise 0. """
    hand_vals = parse_hand(hand, 0)
    trios = find_repeats(hand_vals, 3)

    if not trios:
        return 0

    while(max(trios) in hand_vals):
        hand_vals.remove(max(trios))

    pairs = find_repeats(hand_vals, 2)

    if pairs:
        return 1

    return 0


def four_of_a_kind(hand):
    """ Four of a Kind: Four cards of the same value. Returns the value of the quad. If no quad, return 0. """
    hand_vals = parse_hand(hand, 0)
    quads = find_repeats(hand_vals, 4)

    if len(quads) == 0:
        return 0

    return max(quads)


def straight_flush(hand):
    """ Straight Flush: All cards are consecutive values of same suit. Returns 1 if straight flush, otherwise 0. """

    hv = parse_hand(hand, 0)
    hv.sort()

    hand_suits = hand[1:14:3]

    if hand_suits == len(hand_suits) * hand_suits[0]:
        if hv[1] - hv[0] == 1 and hv[2] - hv[0] == 2 and hv[3] - hv[0] == 3 and hv[4] - hv[0] == 4 :
            return 1

    return 0


def royal_flush(hand):
    """ Royal Flush: Ten, Jack, Queen, King, Ace, in same suit. Returns 1 if royal flush, otherwise 0. """

    hv = parse_hand(hand, 0)
    hv.sort()

    if hv[0] == 10 and hv[1] == 11 and hv[2] == 12 and hv[3] == 13 and hv[4] == 14:
        return 1
    
    return 0


def main():

    count = 0

    raw_list = open("resources/054.txt", "r").read()
    raw_lists = raw_list.split("\n")[0:-1]  # TODO: [0:-1]
    for l in raw_lists:
        
        h1 = l[0:14]
        h2 = l[15:]

        p1 = 0
        p2 = 0

        if royal_flush(h1): p1 = 1
        if royal_flush(h2): p2 = 1
        if p1 > p2:
            count += 1
            continue

        if straight_flush(h1): p1 = 1
        if straight_flush(h2): p2 = 1
        if p1 > p2:
            count += 1
            continue

        if four_of_a_kind(h1) > four_of_a_kind(h2): p1 = 1
        if four_of_a_kind(h1) < four_of_a_kind(h2): p2 = 1
        if p1 > p2:
            count += 1
            continue

        if full_house(h1): p1 = 1
        if full_house(h2): p2 = 1 
        if p1 > p2:
            count += 1
            continue

        if flush(h1): p1 = 1
        if flush(h2): p2 = 1 
        if p1 > p2:
            count += 1
            continue

        if straight(h1): p1 = 1
        if straight(h2): p2 = 1 
        if p1 > p2:
            count += 1
            continue

        if three_of_a_kind(h1) > three_of_a_kind(h2): p1 = 1
        if three_of_a_kind(h1) < three_of_a_kind(h2): p2 = 1
        if p1 > p2:
            count += 1
            continue

        if two_pair(h1) > two_pair(h2): p1 = 1
        if two_pair(h1) < two_pair(h2): p2 = 1
        if p1 > p2:
            count += 1
            continue

        if one_pair(h1) > one_pair(h2): p1 = 1
        if one_pair(h1) < one_pair(h2): p2 = 1
        if p1 > p2:
            count += 1
            continue

        if high_card(h1) > high_card(h2): p1 = 1
        if high_card(h1) < high_card(h2): p2 = 1
        if p1 > p2:
            count += 1
            continue

    return count


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
