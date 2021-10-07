"""
    1. Devide
    2. Merge
"""

def merge(A, p ,q, r):
    i,j = p, q+1
    dummy = []
    while i <= q and j <= r:
        if A[i] < A[j]:
            dummy.append(A[i])
            i += 1
        else :
            dummy.append(A[j])
            j += 1
    if i <= q:
        for a in A[i:q+1]:
            dummy.append(a)
    if j <= r:
        for b in A[j:r+1]:
            dummy.append(b)
    A[p:r+1] = dummy

def mergesort(A, p, r):
    q = (p + r)//2
    if p < r :
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)
    return A

test = [1,5,3,5,8,2,42,21,14]
print(mergesort(test, 0, len(test)-1))