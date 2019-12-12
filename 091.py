import resources.pef as pef
import time
import math
import numpy as np
from itertools import product
"""
https://projecteuler.net/problem=91
37.867307901382446
"""

xy_max = 50
points = list(product(range(0,xy_max+1,1), range(0,xy_max+1,1)))

def is90(p2,p3):
    """
    p2: point in triangle
    p3: point in triangle
    """
    p1 = (0,0)

    # calculate lengths of lines
    len12 = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    len13 = (p1[0] - p3[0])**2 + (p1[1] - p3[1])**2
    len23 = (p2[0] - p3[0])**2 + (p2[1] - p3[1])**2

    try:
        angle1 = math.acos( (len12+len13-len23) / math.sqrt(4*len12*len13) ) * 180/math.pi
        angle2 = math.acos( (len13+len23-len12) / math.sqrt(4*len13*len23) ) * 180/math.pi
        angle3 = math.acos( (len23+len12-len13) / math.sqrt(4*len23*len12) ) * 180/math.pi
        
        if angle1 == 90.0 or angle2 == 90.0 or angle3 == 90.0:
            return True

    except:
        pass

def main():
    total = 0
    for p2 in points:
        for p3 in points:
            if is90(p2, p3):
                total += 1

    return total//2

if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
