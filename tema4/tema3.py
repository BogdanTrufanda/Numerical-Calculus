import json
from pathlib import Path
import copy


def convert(file_name, matrix):
    path = Path("Computing")
    if not path.exists():
        path.mkdir()
    path = path / Path(file_name + ".json")
    with open(path, "w+") as fd:
        json.dump(matrix, fd)


def parse_file(file_name):
    economic_matrix = {}
    with open(file_name, "r") as fd:
        next(fd)
        for line in fd.readlines():
            line = line.strip().split(", ")
            value = float(line[0])
            row = int(line[1])
            column = int(line[2])
            if row not in economic_matrix.keys():
                economic_matrix[row] = {column: value}
            elif column not in economic_matrix[row].keys():
                economic_matrix[row][column] = value
            else:
                economic_matrix[row][column] += value
    return economic_matrix


def aplusb_function(a, b):
    asumb = copy.deepcopy(a)
    for x in b.keys():
        if x not in asumb.keys():
            asumb[x] = b[x]
        else:
            for y in b[x].keys():
                if y not in asumb[x].keys():
                    asumb[x][y] = b[x][y]
                else:
                    asumb[x][y] += b[x][y]

    return asumb


def aorib_function(a, b):
    amultb = {}
    for x_a in a.keys():
        for y_a in a[x_a].keys():
            if y_a in b.keys():
                for y_b in b[y_a].keys():
                    if x_a not in amultb.keys():
                        amultb[x_a] = {y_b: a[x_a][y_a] * b[y_a][y_b]}
                    elif y_b not in amultb[x_a].keys():
                        amultb[x_a][y_b] = a[x_a][y_a] * b[y_a][y_b]
                    else:
                        amultb[x_a][y_b] += a[x_a][y_a] * b[y_a][y_b]

    return amultb


def same_matrices(a, b):
    for x in a.keys():
        if x not in b.keys():
            print(f"The row {x} from matrix A is not in matrix B")
            return False
        for y in a[x].keys():
            if y not in b[x].keys():
                print(f"The column {y} from matrix A is not in matrix B")
                return False
            if a[x][y] != b[x][y]:
                print(
                    f" Value {a[x][y]} from matrix A is NOT the same as value {b[x][y]} from matrix B at position {x}{y}")
                return False
    return True


if __name__ == '__main__':
    a = parse_file("a.txt")
    b = parse_file("b.txt")
    aplusb = parse_file("aplusb.txt")
    aorib = parse_file("aorib.txt")

    convert("a", a)
    convert("b", b)
    convert("aplusb", aplusb)
    convert("aorib", aorib)

    our_aplusb = aplusb_function(a, b)
    our_aorib = aorib_function(a, b)
    convert("our_aplusb", our_aplusb)
    convert("our_aorib", our_aorib)
    print("aplusb = our_aplusb \t", same_matrices(aplusb, our_aplusb))
    print("aorib = our_aorib  \t\t", same_matrices(aorib, our_aorib))
