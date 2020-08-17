from math import sin, cos
import matplotlib.pyplot as plt
import numpy as np
import random


def f(x, a1, a0):
    return a1 * x + a0


def horner(val, x):
    lista = []
    for tmp in x:
        result = val[0]
        for i in range(1, len(val)):
            result = result * tmp + val[i]
        lista.append(result)
    return sum(lista) / len(x)


def calcul_barat(n, val):
    return sum(val) / n


def coef1(n, x, y, x_):
    xlist = 0
    ylist = 0
    for a in range(n):
        xlist += y[a] * (x[a] - x_)
        ylist += x[a] * (x[a] - x_)
    final = xlist / ylist
    return final


def coef0(n, x, y, x_, y_):
    a1_tmp = coef1(n, x, y, x_)
    a0_tmp = y_ - x_ * a1_tmp
    return a1_tmp, a0_tmp


def a_new(n, x, y, x_, y_):
    return coef0(n, x, y, x_, y_)


def show_plot(x, y, name):
    fig = plt.figure()
    fig.suptitle(name, fontsize=16)
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x, y, 'r')
    plt.show()


def t_function(x, a1, a0):
    b1 = 1  # Nu am reusit sa calculam coeficientul b1
    return a0 * 1 + b1 * sin(x) + a1 * cos(x)


def main():
    x0 = 12
    xn = 120
    n = random.randint(2, 10)

    lista = []
    rand = random.randint(x0, xn)
    for _ in range(2 * n + 1):
        lista.append(rand)
        rand = random.randint(int(rand), xn)

    x = np.asarray(sorted(list(set(lista))))
    n = len(x)
    print("n:\t", n)
    print("x:\t", x)

    a1 = random.randint(1, 10)
    a0 = random.randint(1, 10)
    a_list = [a1, a0]
    y = np.asarray([f(val, a1, a0) for val in x])
    print("y:\t", y)

    print("\nReal a1, a0:\t", a1, a0)

    x_ = horner(a_list, x)
    y_ = horner(a_list, y)

    a1_pred, a0_pred = a_new(n, x, y, x_, y_)
    print("Predicted a1, a0:\t", a1_pred, a0_pred)

    s = f(x_, a1_pred, a0_pred)
    print("Sm(x_):\t", s)
    print("Sm(x_) - f(x_):\t{:.20f}".format(s - f(x_, a1, a0)))

    show_plot(x, y, "Function f")

    y_tmp = np.asarray([f(val, a1_pred, a0_pred) for val in x])
    show_plot(x, y_tmp, "Function Sm")

    # p2 = t_function(x_, a1, a0)
    # print(p2)


if __name__ == '__main__':
    main()