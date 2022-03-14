import random
from test_sort import *
import copy

#BFPRT
def gaseste_mediana(vector):
    l = len(vector)
    if len(vector) <=5:
        return sorted(vector)[l >> 1]
    grupuri = [sorted(vector[i:i+5]) for i in range(0, l, 5)]
    mediane = [grup[len(grup) >> 1] for grup in grupuri]

    return gaseste_mediana(mediane)


def index_mediana_din_5(vector, st, dr):
    pivot_list = [random.randint(st, dr) for _ in range(5)]
    pivot_list.sort(key=lambda x:vector[x])
    return pivot_list[2]


def imparte_5(vector, st, dr):
    i = st-1
    index = index_mediana_din_5(vector, st, dr)
    (vector[dr], vector[index]) = (vector[index], vector[dr])
    pivot = vector[dr]
    for j in range(st, dr):
        if vector[j] <= pivot:
            i += 1
            vector[i], vector[j] = vector[j], vector[i]
    vector[i+1], vector[dr] = vector[dr], vector[i+1]
    return i+1


def quick_sort_5(vector, st, dr):
    if st < dr:
        index_impartire = imparte_5(vector, st, dr)
        quick_sort_5(vector, st, index_impartire - 1)
        quick_sort_5(vector, index_impartire + 1, dr)


def imparte_ran(vector, st, dr):
    i = st-1
    index = random.randint(st, dr)
    (vector[dr], vector[index]) = (vector[index], vector[dr])
    pivot = vector[dr]
    for j in range(st, dr):
        if vector[j] <= pivot:
            i += 1
            vector[i], vector[j] = vector[j], vector[i]
    vector[i+1], vector[dr] = vector[dr], vector[i+1]
    return i+1


def quick_sort_ran(vector, st, dr):
    if st < dr:
        index_impartire = imparte_ran(vector, st, dr)
        quick_sort_ran(vector, st, index_impartire - 1)
        quick_sort_ran(vector, index_impartire + 1, dr)

def imparte_mm(vector, st, dr):
    i = st-1
    index = gaseste_mediana(vector)
    (vector[dr], vector[index]) = (vector[index], vector[dr])
    pivot = vector[dr]
    for j in range(st, dr):
        if vector[j] <= pivot:
            i += 1
            vector[i], vector[j] = vector[j], vector[i]
    vector[i+1], vector[dr] = vector[dr], vector[i+1]
    return i+1


def quick_sort_mm(vector, st, dr):
    if st < dr:
        index_impartire = imparte_ran(vector, st, dr)
        quick_sort_ran(vector, st, index_impartire - 1)
        quick_sort_ran(vector, index_impartire + 1, dr)






