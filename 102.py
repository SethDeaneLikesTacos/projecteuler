import resources.pef as pef
import time
"""
https://projecteuler.net/problem=102
0.06700706481933594
"""

def main():

    cnt = 0

    # read array from file and place into 'triangles' array
    # after this block 'triangles' is a 2d list of triangle points
    triangles = []
    tri_list = open("resources/102.txt", "r").read().split('\n')
    for i in tri_list:
        ar = i.split(",")
        ar = [int(j) for j in ar]       # convert strings to ints
        triangles.append(ar)

    for triangle in triangles:

        # setup values with points
        point_a = triangle[0:2]
        point_b = triangle[2:4]
        point_c = triangle[4:6]

        #####
        # Setup area calculations for the three triangles made with origin
        #####
        point_set1 = [0, 0, point_b[0], point_b[1], point_c[0], point_c[1]]
        point_set2 = [0, 0, point_c[0], point_c[1], point_a[0], point_a[1]]
        point_set3 = [0, 0, point_a[0], point_a[1], point_b[0], point_b[1]]
        point_sets = [point_set1, point_set2, point_set3]

        set_area = 0
        for ps in point_sets:
            set_area += abs((ps[0]*(ps[3]-ps[5]) + ps[2]*(ps[5]-ps[1]) + ps[4]*(ps[1]-ps[3])) / 2)

        #####
        # Setup area calculations for entire triangle
        #####
        ts = [point_a[0], point_a[1], point_b[0], point_b[1], point_c[0], point_c[1]]
        tot_area = abs((ts[0]*(ts[3]-ts[5]) + ts[2]*(ts[5]-ts[1]) + ts[4]*(ts[1]-ts[3])) / 2)

        #####
        # Compare are of triangles made with origin with the entiner triangle
        #####
        if set_area == tot_area:
            cnt += 1

    return cnt


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
