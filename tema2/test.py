import copy
import numpy as np


def create_diag(lu, A):
    U = np.triu(lu)
    L = np.tril(lu)
    for x in range(len(A)):
        L[x][x] = 1
    return lu, L, U


def decomposition_lu(A):
    lu = np.zeros((len(A), len(A)))

    for x in range(len(A)):
        if x > 0:
            for y in range(x):
                suma = 0
                for z in range(y):
                    suma = suma + (lu[y][z] * lu[z][x])
                lu[y][x] = (A[y][x] - suma) / lu[y][y]
        for y in range(x + 1):
            suma = 0
            for z in range(y):
                suma = suma + (lu[x][z] * lu[z][y])
            lu[x][y] = A[x][y] - suma
    return create_diag(lu, A)


def x_lu_calculation(lu, b, e):
    x_lu = np.zeros(len(b))
    y_tmp = np.zeros(len(b))
    for x in range(len(b)):
        tmp = 0
        for y in range(x):
            tmp += lu[x][y] * y_tmp[y]
        y_tmp[x] = (b[x] - tmp) / lu[x][x]
    for x in reversed(range(len(b))):
        tmp2 = 0
        for y in range(x + 1, len(b)):
            tmp2 += lu[x][y] * x_lu[y]
        x_lu[x] = y_tmp[x] - tmp2
    return x_lu


if __name__ == '__main__':
    n = 100
    m = 8
    e = pow(10, -m)

    A_init = np.random.rand(n, n)
    b = np.random.rand(n)

    for x in range(n):
        for y in range(n):
            A_init[x][y] *= 100
        b[x] *= 100

    # print("A_init: ", A_init)
    # print("\nB: \t", b)

    A = copy.deepcopy(A_init)
    A, L, U = decomposition_lu(A)

    # print("\nA: ", A)
    # print("\nL: ", L)
    # print("\nU: ", U)

    det_LU = int(np.linalg.det(L)) * int(np.linalg.det(U))
    print("\ndet(A): \t\t\t\t\t{:d}".format(det_LU))

    x_lu = x_lu_calculation(A, b, e)
    # print("\nx_lu:\t\t\t\t\t\t", x_lu)
    dec = np.linalg.norm(np.subtract(np.matmul(A_init, x_lu), b))
    print("A_init * x_lu - b: \t\t\t{:.20f}".format(dec))

    x_lib = np.linalg.solve(A_init, b)
    # print("\nx_lib:\t\t\t\t\t\t", x_lib)
    dec1 = np.linalg.norm(np.subtract(x_lu, x_lib))
    print("x_lu - x_lib: \t\t\t\t{:.20f}".format(dec1))

    A_inv_lib = np.linalg.inv(A_init)
    dec2 = np.linalg.norm(np.subtract(x_lu, np.matmul(A_inv_lib, b)))
    print("x_lu - A_inv_lib * b: \t\t{:.20f}".format(dec2))

    A_inv = np.linalg.inv(A)
    dec3 = np.linalg.norm(np.subtract(A_inv, A_inv_lib))
    print("A_inv - A_inv_lib: \t\t\t{:.20f}".format(dec3))
