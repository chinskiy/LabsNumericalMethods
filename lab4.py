sign = lambda x: x and (1, -1)[x < 0]
transp = lambda matr: list(zip(*matr))


def print_matrix(matr):
    for _ in range(len(matr)):
        for j in range(len(matr[_])):
            print(format(matr[_][j], ',.6f'), end='  ')
        print()
    print()


def find_nu(matr, i, j):
    return 2 * matr[i][j] / (matr[i][i] - matr[j][j])


def find_c(matr, i, j):
    return (0.5 * (1 + 1 / (1 + find_nu(matr, i, j) ** 2) ** 0.5)) ** 0.5


def find_s(matr, i, j):
    return sign(find_nu(matr, i, j)) * (0.5 * (1 - 1 / (1 + find_nu(matr, i, j) ** 2) ** 0.5)) ** 0.5


def find_rotation_matr(matr):
    rotmatr = []
    max_elem = [0, 0, 0]
    for i in range(len(matr)):
        for j in range(len(matr)):
            if j > i:
                if abs(matr[i][j]) > max_elem[0]:
                    max_elem[0], max_elem[1], max_elem[2] = abs(matr[i][j]), i, j
    for i in range(len(matr)):
        tmp = []
        for j in range(len(matr)):
            if i == j:
                tmp.append(1)
            else:
                tmp.append(0)
        rotmatr.append(tmp)
    rotmatr[max_elem[1]][max_elem[1]] = find_c(matr, max_elem[1], max_elem[2])
    rotmatr[max_elem[2]][max_elem[2]] = find_c(matr, max_elem[1], max_elem[2])
    rotmatr[max_elem[2]][max_elem[1]] = find_s(matr, max_elem[1], max_elem[2])
    rotmatr[max_elem[1]][max_elem[2]] = - find_s(matr, max_elem[1], max_elem[2])
    return rotmatr


def mul_matr(matra, matrb):
    res = []
    for i in range(len(matra)):
        tmpres = []
        for j in range(len(matra[i])):
            tmp = 0
            for k in range(len(matra)):
                tmp += matra[i][k] * matrb[k][j]
            tmpres.append(tmp)
        res.append(tmpres)
    return res


def jakobi_meth(matr, epsilon):
    chck = True
    iter = 0
    while chck:
        #print_matrix(matr)
        # print('sph norm: ', format(spherical_norm(matr), ',.4f'), '  ', end='')
        # print('diag sph norm: ', format(diagonal_spherical_norm(matr), ',.4f'), '  ', end='')
        # print('not diag sph norm: ', format(not_diagonal_spherical_norm(matr), ',.4f'), '  ', end='')
        rot_matr = find_rotation_matr(matr)
        matr = mul_matr(mul_matr(transp(rot_matr), matr), rot_matr)
        # print('rot. matrix iter ', iter)
        # print_matrix(rot_matr)
        # print('transp. rot. matrix iter ', iter)
        # print_matrix(transp(rot_matr))
        max_elem = 0
        #print('iter:', iter)
        iter += 1
        for i in range(len(matr)):
            for j in range(len(matr)):
                if j > i:
                    if abs(matr[i][j]) > max_elem:
                        max_elem = abs(matr[i][j])
        if max_elem < epsilon:
            chck = False
    print('result:')
    print_matrix(matr)
    return matr


def diagonal_spherical_norm(matr):
    res = 0
    for i in range(len(matr)):
        for j in range(len(matr)):
            if i == j:
                res += matr[i][j] ** 2
    return res


def not_diagonal_spherical_norm(matr):
    res = 0
    for i in range(len(matr)):
        for j in range(len(matr)):
            if i != j:
                res += matr[i][j] ** 2
    return res


def spherical_norm(matr):
    res = 0
    for i in range(len(matr)):
        for j in range(len(matr)):
            res += matr[i][j] ** 2
    return res


if __name__ == "__main__":
    matrix = [[6.29, 0.97, 1.00, 1.10],
              [0.97, 4.13, 1.30, 0.16],
              [1.00, 1.30, 5.47, 2.10],
              [1.10, 0.16, 2.10, 6.07]]
    #matrix = [[5, 1, 2], [1, 4, 1], [2, 1, 3]]
    # matrix = [[7, 0.88, 0.93, 1.21],
    #           [0.88, 4.16, 1.3, 0.15],
    #           [0.93, 1.3, 6.44, 2],
    #           [1.21, 0.15, 2, 9]]
    eps = 0.0001
    answ = jakobi_meth(matrix, eps)