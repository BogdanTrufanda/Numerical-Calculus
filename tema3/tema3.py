import  json
from  pathlib import Path
import  copy


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


def aplusb_function(asumb, dictval):
    dictvalk = dictval.keys()
    for x in dictvalk:
        asumbk = asumb.keys()
        if x in asumbk:
            ictvalxk = dictval[x].keys()
            for y in ictvalxk:
                asumbxk = asumb[x].keys()
                if y in asumbxk:
                    asumb[x][y] = asumb[x][y] + dictval[x][y]
                else :
                    asumb[x][y] = dictval[x][y]
        else :
            asumb[x] = dictval[x]


def aorib_function(dictval1, dictval2, amultb):
    dictval1k = dictval1.keys()
    for x_a in dictval1k:
        dictval1x_ak = dictval1[x_a].keys()
        for y_a in dictval1x_ak:
            dictval2k = dictval2.keys()
            if y_a in dictval2k:
                dictval2y_ak = dictval2[y_a].keys()
                for y_b in dictval2y_ak:
                    contorkeys = 0
                    keys = amultb.keys()
                    for x in keys:
                        if x_a == x:
                            contorkeys += 1
                    tmp_dict = {}
                    tmp_dict[y_b] = dictval1[x_a][y_a] * dictval2[y_a][y_b]
                    if contorkeys == 0:
                        amultb[x_a] = tmp_dict

                    contorkeys2 = 0
                    keys = amultb[x_a].keys()
                    for x in keys:
                        if y_b == x:
                            contorkeys2 += 1
                    if contorkeys2 == 0:
                        amultb[x_a][y_b] = dictval1[x_a][y_a] * dictval2[y_a][y_b]
                    if contorkeys != 0 and contorkeys2 != 0:
                        amultb[x_a][y_b] = amultb[x_a][y_b] + dictval1[x_a][y_a] * dictval2[y_a][y_b]


def matrici_identice(dictval1, dictval2):
    contor = 0
    dictval1k = dictval1.keys()
    for x in dictval1k:
        dictval1xk = dictval1[x].keys()
        for y in dictval1xk:
            if dictval1[x][y] != dictval2[x][y] or y not in dictval2[x].keys():
                contor += 1
        dictval2k = dictval2.keys()
        if x not in dictval2k:
            contor += 1

    if contor == 0:
        return True
    else:
        return False

def main():
    a = parse_file("a.txt")
    b = parse_file("b.txt")
    aplusb = parse_file("aplusb.txt")
    aorib = parse_file("aorib.txt")

    convert("a", a)
    convert("b", b)
    convert("aplusb", aplusb)
    convert("aorib", aorib)

    asumb = copy.deepcopy(a)
    aplusb_function(asumb, b)
    our_aplusb = asumb
    amultb = {}
    aorib_function(a, b, amultb)
    our_aorib = amultb
    convert("our_aplusb", our_aplusb)
    convert("our_aorib", our_aorib)
    print("aplusb = our_aplusb \t", matrici_identice(aplusb, our_aplusb))
    print("aorib = our_aorib  \t\t", matrici_identice(aorib, our_aorib))

if __name__ == '__main__':
    main()
