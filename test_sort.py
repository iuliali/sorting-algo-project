
def test_sort(v1, v2_sortat):
    #V1 E SORTAT CU SORT DIN PYTHON, v2 cu sortarea mea
    for i in range(len(v1)):
        if v1[i] != v2_sortat[i]:
            return False
    return True