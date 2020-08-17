import numpy as np


def get_matrix_lu(A):
    lu = np.zeros((len(A), len(A)))

    for step in range(len(A)):
        if step > 0:
            for i in range(step):
                s = 0
                for k in range(i):
                    s += lu[i][k] * lu[k][step]
                lu[i][step] = (A[i][step] - s) / lu[i][i]
        for i in range(step + 1):
            s = 0
            for k in range(i):
                s += lu[step][k] * lu[k][i]
            lu[step][i] = A[step][i] - s

    U = np.triu(lu)
    L = np.tril(lu)
    for i in range(len(A)):
        L[i][i] = 1
    return lu, L, U


def compute_x_lu(lu, b, e):
    x_lu = np.zeros(len(b))
    y = np.zeros(len(b))
    for i in range(len(b)):
        if abs(lu[i][i]) > e:
            y[i] = (b[i] - np.sum([lu[i][j] * y[j] for j in range(i)])) / lu[i][i]
    for i in reversed(range(len(b))):
        x_lu[i] = y[i] - np.sum([lu[i][j] * x_lu[j] for j in range(i + 1, len(b))])
    return x_lu


if __name__ == '__main__':
    n = 103
    m = 8
    e = pow(10, -m)

    A = np.random.rand(n, n)
    b = np.random.rand(n)

    # print("A: ", A)
    # print("\nB: \t", b)

    for i in range(n):
        for j in range(n):
            A[i][j] *= 100
        b[i] *= 100

    A_init = A.copy()
    A, L, U = get_matrix_lu(A)

    det_LU = int(np.linalg.det(L)) * int(np.linalg.det(U))
    print("\ndet(A): \t\t\t\t\t{:d}".format(det_LU))

    x_lu = compute_x_lu(A, b, e)
    dec = np.linalg.norm(np.subtract(np.matmul(A_init, x_lu), b))
    print("A_init * x_lu - b: \t\t\t{:.20f}".format(dec))

    x_lib = np.linalg.solve(A_init, b)
    dec1 = np.linalg.norm(np.subtract(x_lu, x_lib))
    print("x_lu - x_lib: \t\t\t\t{:.20f}".format(dec1))

    A_inv_lib = np.linalg.inv(A_init)
    dec2 = np.linalg.norm(np.subtract(x_lu, np.matmul(A_inv_lib, b)))
    print("x_lu - A_inv_lib * b: \t\t{:.20f}".format(dec2))

    A_inv = np.linalg.inv(A)
    dec3 = np.linalg.norm(np.subtract(A_inv, A_inv_lib))
    print("A_inv - A_inv_lib: \t\t\t{:.20f}".format(dec3))
