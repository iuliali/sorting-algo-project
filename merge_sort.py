import random
from test_sort import *

def interclasare(vector, st, mjl, dr):
    i = st
    j = mjl + 1
    vect_aux = []
    while i <= mjl and j <= dr:
        if vector[i] <= vector[j]:
            vect_aux.append(vector[i])
            i += 1
        else:
            vect_aux.append(vector[j])
            j += 1
    vect_aux.extend(vector[i:mjl + 1])
    vect_aux.extend(vector[j:dr + 1])
    vector[st:dr + 1] = vect_aux[:]


def merge_sort(vector, st, dr):
    if dr < st+1: # daca 1 sau 2 elemente
        if dr-st == 1: #2 elem
            if vector[dr] < vector[st]:
                vector[dr] = vector[dr] ^ vector[st]
                vector[st] = vector[dr] ^ vector[st]
                vector[dr] = vector[dr] ^ vector[st]
    else:
        mjl = (st+dr)//2
        merge_sort(vector, st, mjl)
        merge_sort(vector, mjl+1, dr)
        interclasare(vector, st, mjl, dr)




