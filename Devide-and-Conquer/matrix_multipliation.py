# Strassen
"""
    조건 : 2의 제곱에 해당하는 동일한 크기의 정방행렬 두개가 인풋으로 들어가야한다.
    홀수에 대해서는 안전코딩 안했음.
"""
def zero_matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def add_matrix(A, B):
    n = len(A)
    temp = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            temp[i][j] = A[i][j] + B[i][j]

    return temp

def subtract_matrix(A,B):
    n = len(A)
    temp = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            temp[i][j] = A[i][j] - B[i][j]
    return temp


# branch is 8

def make_sub_matrices(X):
    n = len(X)
    k = n//2
    A, B, C, D = zero_matrix(k), zero_matrix(k), zero_matrix(k), zero_matrix(k)

    for i in range(k):
        for j in range(k):
            A[i][j] = X[i][j]
            B[i][j] = X[i][k+j]
            C[i][j] = X[k+i][j]
            D[i][j] = X[k+i][k+j]
    return A, B, C, D

def make_Ps(A,B,C,D,E,F,G,H):
    P1 = strassen(A, subtract_matrix(F, H))
    P2 = strassen(add_matrix(A, B), H)
    P3 = strassen(add_matrix(C, D), E)
    P4 = strassen(D, subtract_matrix(G, E))
    P5 = strassen(add_matrix(A, D), add_matrix(E, H))
    P6 = strassen(subtract_matrix(B,D), add_matrix(G, H))
    P7 = strassen(subtract_matrix(A,C),add_matrix(E,F))
    return P1, P2, P3, P4, P5, P6, P7

def strassen(X, Y):
    n = len(X)
    if n == 1:
        temp = zero_matrix(1)
        temp[0][0] = X[0][0] * Y[0][0]
        return temp
    A,B,C,D = make_sub_matrices(X)
    E,F,G,H = make_sub_matrices(Y)

    P1, P2, P3, P4, P5, P6, P7 = make_Ps(A,B,C,D,E,F,G,H)

    C = zero_matrix(n)

    C11 = add_matrix(subtract_matrix(add_matrix(P5, P4), P2), P6)
    C12 = add_matrix(P1, P2)
    C21 = add_matrix(P3, P4)
    C22 = subtract_matrix(subtract_matrix(add_matrix(P1, P5), P3), P7)

    for i in range(n//2):
        for j in range(n//2):
            C[i][j] = C11[i][j]
            C[i][j + n//2] = C12[i][j]
            C[i + n//2][j] = C21[i][j]
            C[i + n//2][j + n//2] = C22[i][j]

    return C
if __name__ == "__main__":
    test1 = [[i+j for i in range(4)] for j in range(4)]
    test2 = [[i+j for i in range(4)] for j in range(4)]
    print(strassen(test1, test2))
