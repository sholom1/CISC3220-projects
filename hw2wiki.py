from cmath import inf
from math import floor
from typing import List

def MergeSort(S: List[int]) -> List[int]:
    #base case: S is sorted if it's length is <= 1 by definition
    if len(S) <= 1:
        return S
    #split S in half
    midpoint = floor(len(S)/2)
    left = []
    right = []
    for i in range(0, midpoint):
        left.append(S[i])
    for i in range(midpoint, len(S)):
        right.append(S[i])
    #end split
    print(S)
    #sort left side
    left = MergeSort(left)
    print(left)
    #sort right side
    right = MergeSort(right)
    print(right)
    #merge
    return Merge(left, right)

def Merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    #iterate through left and right until one is empty
    #for each iteration compare the front
    #pop appropriate front element into results
    while len(left) > 0 and len(right) > 0:
        if (left[0] < right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    #add any remaining elements to end of result (only one of the list will have elements added)
    result.extend(left)
    result.extend(right)
    return result


a = [2, 1, 6, 3, 4]
a = MergeSort(a)
print(a)