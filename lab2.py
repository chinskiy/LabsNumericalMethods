def print_matrix(matr):
    for _ in range(len(matr)):
        for j in range(len(matr[_])):
            print(format(matr[_][j], ',.4f'), end='  ')
        print()
    print()


def find_main(matr, k):
    a_main = (matr[k][k], (0, 0))
    for _ in range(len(matr)):
        for j in range(len(matr[_]) - 1):
            if a_main[0] < abs(matr[_][j]):
                a_main = (abs(matr[_][j]), (_, j))
    if k != len(matr) - 1:
        temporl.append((k, a_main[1][1]))
        matr[k], matr[a_main[1][0]] = matr[a_main[1][0]], matr[k]
        for _ in range(len(matr)):
            matr[_][k], matr[_][a_main[1][1]] = matr[_][a_main[1][1]], matr[_][k]


def find_m_fact(matr, k):
    m_factors = []
    for _ in range(len(matr)):
        m_factors.append(matr[_][k] / matr[k][k])
    return m_factors


def substract_m_fact(matr, m_factors, k):
    for _ in range(len(matr)):
        for j in range(len(matr[_])):
            if _ > k:
                matr[_][j] -= m_factors[_] * matr[k][j]
    temp = matr[k][k]
    for _ in range(len(matr) + 1):
        matr[k][_] = matr[k][_] / temp + 0
    return matr


def find_converse(matr):
    matr.reverse()
    for _ in range(len(matr)):
        matr[_].reverse()
    answ = []
    for _ in range(len(matr)):
        temp_answ = 0
        for j in range(_ + 1):
            if j == 0:
                temp_answ = matr[_][0]
            else:
                temp_answ -= matr[_][j] * answ[j - 1]
        answ.append(temp_answ)
    return answ


def find_solution_slar(matr):
    i = 0
    while len(matr) > i:
        find_main(matr, i)
        print_matrix(matrix)
        substract_m_fact(matr, find_m_fact(matr, i), i)
        #print_matrix(matrix)
        i += 1
    print_matrix(matrix)
    solut = find_converse(matr)
    for el in temporl:
        solut[el[1]], solut[el[0]] = solut[el[0]], solut[el[1]]
    return solut


def find_vector_of_discrepancy(matr, answ):
    vect = []
    for _ in range(len(matr)):
        tmp = 0
        for j in range(len(matr[_]) - 1):
            tmp += matr[_][j] * answ[j]
        vect.append(tmp)
    answer = []
    for _ in range(len(vect)):
        answer.append(matr[_][len(matr)] - vect[_])
    for el in answer:
        print(format(el, ',.16f'), end='  ')


if __name__ == "__main__":
    temporl = []
    matrix = [[8.30, 2.62, 4.10, 1.90, -10.65],
             [3.92, 8.45, 8.78, 2.46, 12.21],
             [3.77, 7.21, 8.04, 2.28, 15.45],
             [2.21, 3.65, 1.69, 6.9, -8.35]]
    print_matrix(matrix)
    solution = find_solution_slar(matrix)
    for elem in solution:
        print(format(elem, ',.4f'), end='  ')
    print()
    matrix2 = [[8.30, 2.62, 4.10, 1.90, -10.65],
              [3.92, 8.45, 8.78, 2.46, 12.21],
              [3.77, 7.21, 8.04, 2.28, 15.45],
              [2.21, 3.65, 1.69, 6.9, -8.35]]
    find_vector_of_discrepancy(matrix2, solution)