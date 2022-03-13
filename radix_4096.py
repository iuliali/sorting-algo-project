import math
import random
from time import time
from test_sort import *
from radix_sort import *

def radix_4096(vector):
    BAZA = 4096
    P_BAZEI = 12
    maxim = math.floor(math.log(max(vector), 4096)+1)
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
