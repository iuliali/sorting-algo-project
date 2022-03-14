from time import time
# from test_sort import test_sort
# from radix_1024 import *
# from radix_65536 import *
# from radix_256 import *
from radix_4096 import *
from merge_sort import *
from shell_sort import *
from heap_sort import *
from quick_sort import *
import random
import copy


def CustomInput(A, max, N):
    fout.write(f"10^{int(math.log10(N))} numere cu maximul 10^{int(math.log10(max))}: \n")
    # A1 = copy.deepcopy(A)
    # A2 = copy.deepcopy(A)
    A3 = copy.deepcopy(A)
    A4 = copy.deepcopy(A)
    A5 = copy.deepcopy(A)
    A6 = copy.deepcopy(A)
    # A7 = copy.deepcopy(A)
    # A8 = copy.deepcopy(A)
    # A9 = copy.deepcopy(A)


    fout.write("Default Sort PYTHON3 \n")
    start = time()
    A.sort()
    stop = time()
    fout.write(f"       Timp: {stop - start}\n")


    fout.write("Merge Sort \n")
    try:
        start = time()
        merge_sort(A3, 0, N - 1)
        stop = time()
        fout.write(f"       Timp: {stop - start}\n")
        fout.write(f"       Corect sortat: {test_sort(A, A3)}\n")
    except RecursionError:
        fout.write("Nu pot Sorta ! E prea multa recursie")
        fout.write("\n")

    fout.write("Shell Sort Marcin Ciura \n")
    start = time()
    shell_sort(A4, gaps_ciura)
    stop = time()
    fout.write(f"       Timp: {stop - start}\n")
    fout.write(f"       Corect sortat: {test_sort(A, A4)}\n")

    fout.write("Shell Sort 2^k+1 \n")
    start = time()
    shell_sort(A5, gap_generator_2(N))
    stop = time()
    fout.write(f"       Timp: {stop - start}\n")
    fout.write(f"       Corect sortat: {test_sort(A, A5)}\n")

    fout.write("Shell Sort 3k+1 \n")
    start = time()
    shell_sort(A6, gap_generator_1(N))
    stop = time()
    fout.write(f"       Timp: {stop - start}\n")
    fout.write(f"       Corect sortat: {test_sort(A, A6)}\n")

    # fout.write("Heap Sort \n")
    # start = time()
    # heap_sort(A7)
    # stop = time()
    # fout.write(f"       Timp: {stop - start}\n")
    # fout.write(f"       Corect sortat: {test_sort(A, A7)}\n")
    #
    # fout.write("Quick Sort - pivot random \n")
    # try:
    #     start = time()
    #     quick_sort_ran(A8,0,N-1)
    #     stop = time()
    #     fout.write(f"       Timp: {stop - start}\n")
    #     fout.write(f"       Corect sortat: {test_sort(A, A8)}\n")
    #     fout.write("\n")
    # except RecursionError:
    #     fout.write("Nu pot Sorta ! E prea multa recursie")
    #     fout.write("\n")


    # fout.write("Quick Sort - mediana din 5 \n")
    # try:
    #     start = time()
    #     quick_sort_ran(A9,0,N-1)
    #     stop = time()
    #     fout.write(f"       Timp: {stop - start}\n")
    #     fout.write(f"       Corect sortat: {test_sort(A, A9)}\n")
    #     fout.write("\n")
    # except RecursionError:
    #     fout.write("Nu pot Sorta ! E prea multa recursie")
    #     fout.write("\n")


fout = open("teste3.out", "a")
fin = open("teste_shell.in","r")
nr_teste = int(fin.readline())
params_tests = []
for i in range(nr_teste):
    linie = fin.readline().split()
    params_tests.append((int(linie[0]), int(linie[1])))


# for k in range(nr_teste):
k=4
N = params_tests[k][0]
max = params_tests[k][1]
A = [random.randint(0, max) for _ in range(N)]
CustomInput(A, max, N)