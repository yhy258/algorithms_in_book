import random

def quicksort(A):
    if len(A) <= 1 : return A
    left, right, equal = [],[], []
    pivot = A[len(A)//2]
    for i in range(len(A)):
        if pivot > A[i]:
            left.append(A[i])
        elif pivot == A[i]:
            equal.append(A[i])
        else :
            right.append(A[i])

    return quicksort(left) + equal + quicksort(right)

test = [7,3,2,5,9,4,2]
print(quicksort(test))