import math
import random
from time import time
from test_sort import *
from radix_sort import *

def radix_65536(vector):
    BAZA = 65536
    P_BAZEI = 16
    maxim = math.floor(math.log(max(vector), BAZA)+1)
    solutie_temp = [0] * len(vector)

    for p in range(maxim):
        resturi_posibile = [0] * BAZA
        for i in range(0, len(vector)):
            rest = (vector[i] >> (P_BAZEI*p)) & (BAZA - 1)
            resturi_posibile[rest] += 1

        for k in range(1, BAZA):
            resturi_posibile[k] += resturi_posibile[k-1]

        for index in range(len(vector)-1, -1, -1):
            rest = (vector[index] >> (P_BAZEI * p)) & (BAZA - 1)
            resturi_posibile[rest] -= 1
            solutie_temp[resturi_posibile[rest]] = vector[index]

        for x in range(len(vector)):
            vector[x] = solutie_temp[x]

    return vector


# A=[random.randint(0, 100000) for i in range(100000)]
# start = time()
# B = radix_65536(A)
# stop = time()
# print(stop-start)
# print(test_sort(A,B))
#
#
# start = time()
# radix_sort(A, 65536)
# stop = time()
# print(stop-start)
#
# start = time()
# A.sort()
# stop = time()
# print(stop-start)