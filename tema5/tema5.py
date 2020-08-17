import  json
import  random
from pathlib import Path
import numpy as np


def convert(file_name, matrix):
    path = Path("Computing")
    if not path.exists():
        path.mkdir()
    path = path / Path(file_name + ".json")
    with open(path, "w+") as fd:
        json.dump(matrix, fd, indent=1)


def parse_file(file_name):
    economic_matrix = {}
    with open(file_name, "r") as fd:
        next(fd)
        for x in fd.readlines():
            x = x.rstrip()
            x = x.split(",")
            # print(x)
            value = float(x[0])
            row = int(x[1])
            column = int(x[2])

            contorkeys = 0
            keys = economic_matrix.keys()
            for x in keys:
                if row == x:
                    contorkeys += 1
            tmp_dict = {}
            tmp_dict[column] = value
            if contorkeys == 0:
                economic_matrix[row] = tmp_dict

            contorkeys2 = 0
            keys = economic_matrix[row].keys()
            for x in keys:
                if column == x:
                    contorkeys2 += 1
            if contorkeys2 == 0:
                economic_matrix[row][column] = value

    return economic_matrix

def generate_matrix(marime):
    path = Path(__file__).resolve().parent / "RareMatrix"
    if not path.exists():
        path.mkdir()
    string = "_" + str(marime) + ".txt"
    with open(str(path) + "/rare_matrix" + string, "w+") as fd:
        fd.write(str(marime))
        fd.write(str("\n"))
        for x in range(marime):
            for y in range(marime):
                tmp = random.random()
                if tmp > 99 / 100:
                    tmp2 = random.randint(1, marime)
                    string = str(tmp2) + ", " + str(x) + ", " + str(y) + "\n"
                    fd.write(string)
                    string = str(tmp2) + ", " + str(y) + ", " + str(x) + "\n"
                    fd.write(string)


def check_symmetric(matrix):
    for index, key in matrix.items():
        for index2, key2 in key.items():
            if abs(matrix[index][index2] - matrix[index2][index]) > 0.000000001:
                return  False
    return  True


def convert_matrix(file_name):
    with open(file_name, "r") as fd:
        size = int(fd.readline())
        mat = np.zeros((size, size), dtype=int)
        for x in fd.readlines():
            if x != "\n":
                x = x.rstrip()
                x = x.split(",")
                value = float(x[0])
                row = int(x[1])
                column = int(x[2])
                mat[row][column] = value
    return  mat


def ownvalues(A, v):
    w = A.dot(v)
    return v.dot(w)


def power_method(A, k=-15):
    n = len(A)
    x = np.random.rand(n)
    v = x / np.linalg.norm(x)
    delta = ownvalues(A, v)

    for x in range(1000000):
        w = A.dot(v)
        new_v = w / np.linalg.norm(w)

        new_delta = ownvalues(A, new_v)
        if np.abs(np.subtract(delta, new_delta)) < n * pow(10, k):
            return new_delta, new_v

        v = new_v
        delta = new_delta

    k += 1
    print("K:\t", k)
    if k == -8:
        print("No value found!")
    else:
        power_method(A, k)


def generate_Aandb(p, n):
    A = np.random.rand(p, n)
    b = np.random.rand(p)

    for x in range(p):
        for y in range(n):
            A[x][y] *= 100
        b[x] *= 100

    return A, b


def point_C():
    A, b = generate_Aandb(20, 10)
    print(np.linalg.svd(A))
    print(np.linalg.matrix_rank(A))
    print(np.linalg.cond(A))
    moore = np.linalg.pinv(A)
    print(moore)
    x = moore.dot(b)
    dec = np.linalg.norm(np.subtract(b, A.dot(x)))
    print("b1 - A_init1 * x_lu1: \t\t\t{:.20f}".format(dec))

    dec = np.linalg.norm(np.subtract(moore, np.linalg.inv(A.transpose().dot(A)).dot(A.transpose())))
    print("A^i - A^j: \t\t\t{:.20f}".format(dec))


def main():
    # Point A
    a_300 = parse_file("a_300test.txt")
    a_500 = parse_file("a_500test.txt")
    a_1000 = parse_file("a_1000test.txt")
    a_1500 = parse_file("a_1500test.txt")
    a_2020 = parse_file("a_2020test.txt")
    if not Path("Computing/a_300.json").exists():
        convert("a_300", a_300)
    if not Path("Computing/a_500.json").exists():
        convert("a_500", a_500)
    if not Path("Computing/a_1000.json").exists():
        convert("a_1000", a_1000)
    if not Path("Computing/a_1500.json").exists():
        convert("a_1500", a_1500)
    if not Path("Computing/a_2020.json").exists():
        convert("a_2020", a_2020)

    lungime = [a_300, a_500, a_1000, a_1500, a_2020]
    for index in lungime:
        if len(index) > 500:
            generate_matrix(len(index))

    rare_matrix_1000 = parse_file("RareMatrix/rare_matrix_1000.txt")
    rare_matrix_1500 = parse_file("RareMatrix/rare_matrix_1500.txt")
    rare_matrix_2020 = parse_file("RareMatrix/rare_matrix_2020.txt")
    if not Path("Computing/rare_matrix_1000.json").exists():
        convert("rare_matrix_1000", rare_matrix_1000)
    if not Path("Computing/rare_matrix_1500.json").exists():
        convert("rare_matrix_1500", rare_matrix_1500)
    if not Path("Computing/rare_matrix_2020.json").exists():
        convert("rare_matrix_2020", rare_matrix_2020)

    # Point B
    print("Rare matrix 1000 is symmetric:\t", check_symmetric(rare_matrix_1000))
    print("Rare matrix 1500 is symmetric:\t", check_symmetric(rare_matrix_1500))
    print("Rare matrix 2020 is symmetric:\t", check_symmetric(rare_matrix_2020))
    print("A 300 is symmetric:\t", check_symmetric(a_300))
    print("A 500 is symmetric:\t", check_symmetric(a_500))
    print("A 1000 is symmetric:\t", check_symmetric(a_1000))
    print("A 1500 is symmetric:\t", check_symmetric(a_1500))
    print("A 2020 is symmetric:\t", check_symmetric(a_2020))

    # print("Rare matrix 1000:\n", power_method(convert_matrix("RareMatrix/rare_matrix_1000.txt")))
    # print("Rare matrix 1500:\n", power_method(convert_matrix("RareMatrix/rare_matrix_1500.txt")))
    # print("Rare matrix 2020:\n", power_method(convert_matrix("RareMatrix/rare_matrix_2020.txt")))
    # print("A 300:\n", power_method(convert_matrix("a_300test.txt")))
    # print("A 500:\n", power_method(convert_matrix("a_500test.txt")))
    # print("A 1000:\n", power_method(convert_matrix("a_1000test.txt")))
    # print("A 1500:\n", power_method(convert_matrix("a_1500test.txt")))
    # # print("A 2020:\n", power_method(convert_matrix("a_2020test.txt")))

    # Point C
    # point_C()


if __name__ == '__main__':
    main()
