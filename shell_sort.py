import math

from test_sort import *
import random

def gap_generator_1(l):
    x = 1
    gap_seq = []
    while(x < l//3):
        gap_seq.append(x)
        x = 3*x + 1
    return gap_seq

def gap_generator_2(l):
    k = 1
    elem = 1
    gap_seq = []
    while(elem < l//100):
        gap_seq.append(elem)
        elem = (1 << k) +1
        k += 1
    return gap_seq


def shell_sort(vector, gap_seq):
    print(gap_seq)
    lungime = len(vector)
    k = len(gap_seq)-1
    for h in gap_seq[::-1]:
        for i in range(h, lungime):
            j=i
            while j >= h and vector[j] < vector[j-h]: #insertion sort pe subvectorul creat de val gap curenta
                vector[j] = vector[j] ^ vector[j-h]
                vector[j-h] = vector[j] ^ vector[j-h]
                vector[j] = vector[j] ^ vector[j-h]
                j -= h
    return vector

gaps = [1, 4, 10, 23, 57, 132, 301, 701]

# A= [random.randint(1,10000000) for _ in range(10000)]
# print(len(A))
# shell_sort(A,gap_generator(len(A)))
# shell_sort()
# print(A)
# print(test_sort(A, A))
# print(gap_generator_2(5000))


