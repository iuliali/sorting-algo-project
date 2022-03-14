
def reheap(vector, l, rdx):

    maxim_desc = rdx
    st = (rdx << 1) + 1
    dr = (rdx << 1) + 2
    # sa vad daca exista desc imediati si daca e vreunul mai mare decat rdx actual
    if dr < l:
        if vector[dr] > vector[maxim_desc]:
            maxim_desc = dr
    if st < l:
        if vector[st] > vector[maxim_desc]:
            maxim_desc = st

    if vector[rdx] < vector[maxim_desc]:
        vector[rdx] = vector[rdx] ^ vector[maxim_desc]
        vector[maxim_desc] = vector[rdx] ^ vector[maxim_desc]
        vector[rdx] = vector[rdx] ^ vector[maxim_desc]
        reheap(vector, l, maxim_desc)

def heap_sort(vector):
    lungime = len(vector)

    for i in range((lungime >> 1)-1, -1, -1):
        reheap(vector, lungime, i)

    for i in range(lungime-1, 0, -1): #extrag de n-1 ori maximul din max heap
        vector[i] = vector[i] ^ vector[0]
        vector[0] = vector[i] ^ vector[0]
        vector[i] = vector[i] ^ vector[0]
        reheap(vector, i, 0)




