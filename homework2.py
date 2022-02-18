from math import floor, inf

def MergeSort(array, p, r):
    if p < r:
        q = floor((p + r) / 2)
        MergeSort(array, p, q)
        MergeSort(array, q + 1, r)
        Merge(array, p, q, r)

def Merge(array, p, q, r):
    n1 = q-p
    n2 = r-q
    L = []
    R = []
    for i in range(0, n1):
        L.append(array[p + i])
    for j in range(0, n2):
        R.append(array[q + j])
    L.append(inf)
    R.append(inf)
    i = 0
    j = 0
    for k in range(p, r):
        if (L[i] < R[j]):
            array[k] = L[i]
            i = i + 1
        else:
            array[k] = R[j]
            j = j + 1

a = [2, 1, 6, 3, 4]
print (a)
MergeSort(a, 0, len(a) - 1)
print(a)