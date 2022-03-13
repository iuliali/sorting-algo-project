
def test_sort(v1, v2_sortat):
    v1.sort()
    # print(v2_sortat)
    for i in range(len(v1)):
        if v1[i] != v2_sortat[i]:
            return False
    return True