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
fout = open("teste_variante_input_2.out", "a")

N1 = 10**6
max1 = 10**6
max2 = 10**3
N3 = 10**6
max3 = 10**10


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




# spread
fout.write("     ORDINE COMPLET ALEATORIE:\n")
A = [random.randint(0, max1) for _ in range(N1)]
CustomInput(A,max1,N1)

# sortat desc
fout.write("     SORTAT DESCRESCATOR: \n")
B = copy.deepcopy(A)
B.sort(reverse=True)
CustomInput(B,max1,N1)


# aproape sortat
fout.write("     APROAPE SORTAT : ")
C = copy.deepcopy(A)
C.sort()

for i in range(10):  # fac niste inversiuni in vectorul sortat
    a, b = random.randint(0, N1 - 1), random.randint(0, N1 - 1)
    C[a], C[b] = C[b], C[a]
CustomInput(C,max1,N1)



# multe nr putine valori
fout.write(f"{N1} numere cu maximul {max2} --")
D = [random.randint(0, max2) for _ in range(N1)]
CustomInput(D,max2,N1)


# multe valori putine nr
fout.write(f"{N3} numere cu maximul {max3} --")
E = [random.randint(0, max3) for _ in range(N3)]
CustomInput(E,max3,N3)

fout.close()