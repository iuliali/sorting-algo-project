from time import time
from test_sort import test_sort
from radix_1024 import *
from radix_65536 import *
from radix_256 import *
from radix_4096 import *
from merge_sort import *
from shell_sort import *
from heap_sort import *
from quick_sort import *
import copy


def CustomInput(A, max, N):
    fout.write(f"10^{int(math.log10(N))} numere cu maximul 10^{int(math.log10(max))}: \n")

    A1 = copy.deepcopy(A)
    A2 = copy.deepcopy(A)
    A3 = copy.deepcopy(A)
    A4 = copy.deepcopy(A)
    A5 = copy.deepcopy(A)
    A6 = copy.deepcopy(A)
    A7 = copy.deepcopy(A)
    A8 = copy.deepcopy(A)
    A9 = copy.deepcopy(A)


    fout.write("Default Sort PYTHON3 \n")
    start = time()
    A.sort()
    stop = time()
    fout.write(f"       Timp: {stop - start}\n")

    fout.write("Radix 2^10 \n")
    start = time()
    radix_1024(A1)
    stop = time()
    fout.write(f"       Timp: {stop - start}\n")
    fout.write(f"       Corect sortat: {test_sort(A, A1)}\n")

    fout.write("Radix 2^12 \n")
    start = time()
    radix_4096(A2)
    stop = time()
    fout.write(f"       Timp: {stop - start}\n")
    fout.write(f"       Corect sortat: {test_sort(A, A2)}\n")

    fout.write("Radix 2^16 \n")
    start = time()
    radix_65536(A3)
    stop = time()
    fout.write(f"       Timp: {stop - start}\n")
    fout.write(f"       Corect sortat: {test_sort(A, A3)}\n")

    fout.write("Merge Sort \n")
    try:
        start = time()
        merge_sort(A4, 0, N - 1)
        stop = time()
        fout.write(f"       Timp: {stop - start}\n")
        fout.write(f"       Corect sortat: {test_sort(A, A4)}\n")
    except RecursionError:
        fout.write("Nu pot Sorta ! E prea multa recursie")
        fout.write("\n")

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

    fout.write("Heap Sort \n")
    start = time()
    heap_sort(A7)
    stop = time()
    fout.write(f"       Timp: {stop - start}\n")
    fout.write(f"       Corect sortat: {test_sort(A, A7)}\n")

    fout.write("Quick Sort - pivot random \n")
    try:
        start = time()
        quick_sort_ran(A8,0,N-1)
        stop = time()
        fout.write(f"       Timp: {stop - start}\n")
        fout.write(f"       Corect sortat: {test_sort(A, A8)}\n")
        fout.write("\n")
    except RecursionError:
        fout.write("Nu pot Sorta ! E prea multa recursie")
        fout.write("\n")


    fout.write("Quick Sort - mediana din 5 \n")
    try:
        start = time()
        quick_sort_ran(A9,0,N-1)
        stop = time()
        fout.write(f"       Timp: {stop - start}\n")
        fout.write(f"       Corect sortat: {test_sort(A, A9)}\n")
        fout.write("\n")
    except RecursionError:
        fout.write("Nu pot Sorta ! E prea multa recursie")
        fout.write("\n")


fout = open("teste2.out", "a")
fin = open("teste.in","r")
nr_teste = int(fin.readline())
params_tests = []
for i in range(nr_teste):
    linie = fin.readline().split()
    params_tests.append((int(linie[0]), int(linie[1])))

for k in range(nr_teste):
    N = params_tests[k][0]
    max = params_tests[k][1]
    A = [random.randint(0, max) for _ in range(N)]
    CustomInput(A, max, N)








