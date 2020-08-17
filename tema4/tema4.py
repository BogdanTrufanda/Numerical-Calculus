import tema3
import math


def infinity_norm(x):
    """
    Compute infinity norm of x.
    :param x: rare matrix represented as dictionary of dictionaries of non zero values
    :return max_value: maximum value of x
    """
    max_value = None
    for line in x.keys():
        for column in x[line].keys():
            if not max_value or max_value < x[line][column]:
                max_value = x[line][column]
    return max_value


def check_values_on_diagonal(matrix):
    """
    Checks if a matrix made out of dictionary of dictionaries has values on diagonal
    :param matrix: dictionary of dictionaries
    :return: boolean
    """
    for line in matrix.keys():
        if line not in matrix[line].keys():
            return False
    return True


def get_x_sor(a, b, size, check_det, omega, max_iterations=1000, epsilon=pow(10, -10)):
    if omega >= 2 or omega <= 0:
        print("[ERROR]: Omega should be in interval (0, 2).")
        return None
    if check_det is False:
        print("[ERROR]: Cannot compute x using SOR.")
        return None
    ok = False
    iterations = 0
    x_sor = homework3.create_x(size, 0)
    norm = 0
    while iterations < max_iterations:
        norm = 0
        for line in range(size):
            sums = 0
            save = x_sor[line][0]
            for column in a[line].keys():
                sums += a[line][column] * x_sor[column][0]
            x_sor[line][0] += (omega / a[line][line]) * (b[line][0] - sums)
            norm += pow(x_sor[line][0] - save, 2)
        norm = math.sqrt(norm)
        if norm < epsilon:
            break
        if norm > pow(10, 8):
            break
        iterations += 1
    if norm < epsilon:
        print("Approximated value: {}".format(x_sor))
        ok = True
    else:
        print("[ERROR]: Divergence.")
        if iterations >= max_iterations:
            print("\t[WARNING]: Reached maximum iterations. Stopping the computation.\n\t[SUGGESTION]: Lower epsilon.")
        if norm > pow(10, 8):
            print(
                "\t[WARNING]: Norm bigger than 10^8. Stopping the computation.\n\t[SUGGESTION]: Change omega or method.")
            print("\tNorm:", norm)
    print("Iterations: {}".format(iterations))
    return (x_sor, ok)


if __name__ == '__main__':
    omegas = [0.8, 1.0, 1.2]
    for index in range(5):
        exec(
            "matrix_{}, vector_{}, size_{} = homework3.extract_data(\"m_rar_2019_{}.txt\")".format(index + 1, index + 1,
                                                                                                   index + 1,
                                                                                                   index + 1))
        exec("print(\"Size for matrix {}:\", size_{})".format(index + 1, index + 1))
        exec("homework3.to_json(\"matrix_{}\", matrix_{})".format(index + 1, index + 1))
        exec("check_{} = check_values_on_diagonal(matrix_{})".format(index + 1, index + 1))
        exec("print(\"Values on diagonal for matrix {}:\", check_{})".format(index + 1, index + 1))
        for index_omegas in range(len(omegas)):
            exec("result_{} = get_x_sor(matrix_{}, vector_{}, size_{}, check_{}, {})".format(index_omegas, index + 1,
                                                                                             index + 1, index + 1,
                                                                                             index + 1,
                                                                                             omegas[index_omegas]))
            exec("if True in result_{}: print('Norm check:', infinity_norm(homework3.subtraction("
                 "homework3.multiplication(matrix_{}, result_{}[0]), vector_{})))".format(index_omegas, index + 1,
                                                                                          index_omegas, index + 1))
            exec("if True in result_{}: homework3.to_json(\"result_{}_{}\", result_{}[0])".format(index_omegas,
                                                                                                  index + 1,
                                                                                                  index_omegas + 1,
                                                                                                  index_omegas))
        print("-----------------------------------------------------------------------------------")
        input()
