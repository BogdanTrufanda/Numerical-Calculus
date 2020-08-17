# 1.Să se găsească cel mai mic număr pozitiv u > 0, de forma u = 10^(-m) care satisface
# proprietatea: 1+ u != 1
import math
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)


u = +math.inf
for i in range(100):
    tmp = 10 ** (-i)
    if tmp + 1 != 1:
        if tmp < u:
            u = tmp
print("u:\t%.52f" % u)
# 2. Operația + este neasociativă: fie numerele x=1.0 , y = u , z = u, unde u este precizia mașină calculată anterior.
# Să se verifice că operația de adunare efectuată de calculator
# este neasociativă: (x + y) + z != x + (y + z)
# Să se găsească un exemplu pentru care operația de înmulțire * este neasociativă.
x, y, z = 1.0, u, u
if (x + y) + z != x + (y + z):
    print(True)
else:
    print(False)

x, y, z = u, u, u
if (y * z) * (-10 * x) != y * (z * (-10 * x)):
    print(True)
else:
    print(False)

# 3.
n = 7
print("\nN:\t", n)
m = int(math.log2(n))
print("M:\t", m)
p = n // m
print("P:\t", p)

a = [np.random.randint(2, size=(n, n))]
b = [np.random.randint(2, size=(n, n))]


# print(a, end="\n\n")
# print(b)


def impartire(a, lc):
    maxim = 0
    for i in range(1, p):
        tmp = []
        for x in range(m * (i - 1) + 1, m * i + 1):
            if x > maxim:
                maxim = x
            if lc == 0:
                tmp.append(a[0][:, x - 1])
            else:
                tmp.append(a[0][x - 1, :])
        a.append(np.array(tmp))
    tmp = []
    for i in range(maxim + 1, n + 1):
        if lc == 0:
            tmp.append(a[0][:, i - 1])
        else:
            tmp.append(a[0][i - 1, :])
    if len(tmp) != m - 1:
        tmp.append(np.array([0 for _ in range(n)]))
    a.append(np.array(tmp))

    if lc == 0:
        for i in range(1, p + 1):
            tmp = []
            for j in range(n):
                tmp.append(a[i][:, j])
            a[i] = np.array(tmp)
    return a


def sum_matrix(a, b):
    # print(a)
    # print(b)
    # print()
    lfinala = []
    for x in a:
        x = x.tolist()
        if x.count(1) == 0:
            lfinala.append([0] * len(b[0]))
        if x.count(1) == 1:
            pozitie = x.index(1)
            lfinala.append(b[pozitie])
        elif x.count(1) > 0:
            tmp = []
            for y in enumerate(x):
                if y[1] == 1:
                    tmp.append(b[y[0]])
            suma = [sum(x) for x in zip(*tmp)]
            suma = [1 if suma[x] >= 1 else 0 for x in range(len(suma))]
            lfinala.append(suma)
    # print(np.array(lfinala))
    # print("\n")
    return lfinala


a = impartire(a, 0)
b = impartire(b, 1)

print("A"*30)
for i in a:
    print(i, end="\n\n")
print("B"*30)
for i in b:
    print(i, end="\n\n")


c = [np.zeros((n, n), dtype=int)]
for i in range(1, p + 1):
    c.append(np.array(sum_matrix(a[i], b[i])))

# for k in range(1, p + 1):
#     for i in range(n):
#         for j in range(n):
#             if c[0][i][j] + c[k][i][j] >= 1:
#                 c[0][i][j] = 1

for k in range(1, p + 1):
    c[0] = np.add(c[0], c[k])
c[0][c[0] > 1] = 1
print("C"*30)
print(c[0])

print()
print(a[0].dot(b[0]))