def insertionSort(sequence = [], startIndex = 1):
    for j in range(startIndex, len(sequence)):
        key = sequence[j]
        i = j-1
        while i >= 0 and sequence[i] < key:
            sequence[i+1] = sequence[i]
            i = i - 1
        sequence[i + 1] = key

A = [2, 8, 4, 3, 1, 6, 3 ]
print(A)
insertionSort(A)
print(A)