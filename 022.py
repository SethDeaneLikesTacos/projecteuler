import pef
import time
"""
Using names.txt (right click and 'Save Link/Target As...'), a
46K text file containing over five-thousand first names, begin
by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position
in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def main():
    start_time = time.time()

    total = 0
    names = open("resources/022.txt", "r").read().replace('"', "").split(',')
    names.sort()
    
    for name in names:
        i = names.index(name) + 1

        namesum = 0
        for letter in name:
            namesum += ord(letter) - 64
        namesum = namesum * i
        total += namesum

    end_time = time.time()
    pef.answer(total, end_time - start_time)

main()
