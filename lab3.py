def print_matrix(matr):
    for _ in range(len(matr)):
        for j in range(len(matr[_])):
            print(format(matr[_][j], ',.4f'), end='  ')
        print()
    print()


def find_diagonal_preference(matr):
    matr_diag_pref = []
    for i in range(len(matr)):
        tmp = []
        for j in range(len(matr[i])):
            if i != j:
                tmp.append(- (matr[i][j] / (matr[i][i])))
            else:
                tmp.append(0)
        matr_diag_pref.append(tmp)
    return matr_diag_pref


def get_d(matra, matrb):
    d = []
    for i in range(len(matrb)):
        d.append(matrb[i] / matra[i][i])
    return d


def iteration(matra, matrb, diag_pref):
    d = get_d(matra, matrb)
    x = [0 for _ in range(len(matrb))]
    xk1 = [0 for _ in range(len(matrb))]
    k = 0
    chck = True
    while chck:
        print("iteration:", k)
        k += 1
        for i in range(len(matrb)):
            xk1[i] = d[i]
            for j in range(len(matra)):
                if i != j:
                    xk1[i] += diag_pref[i][j] * x[j]
            chck = check(x, xk1)
            x[i] = xk1[i]
        print('result:', end='   ')
        for _ in x:
            print(format(_, ',.4f'), end=' ')
        print()
        nev(matra, x, matrb)
    return x


def check(a, b):
    ch = []
    for i in range(len(a)):
        ch.append(b[i] - a[i])
    if max(ch) < eps:
        return False
    return True


def nev(matra, x, matrb):
    nevyazka = []
    print('Nevyazka:', end='  ')
    for i in range(len(matra)):
        summ = 0
        for j in range(len(matra)):
            summ += matra[i][j] * x[j]
        nevyazka.append(matrb[i] - summ)
        print(format(nevyazka[i], ',.4f'), end=' ')
    print()
    return nevyazka


if __name__ == "__main__":
    A = [[8.00, 0.14, 2.62, 1.54],
         [0.15, 1.24, 0.74, 0.18],
         [2.87, -0.23, 3.6, 1.20],
         [1.76, -0.07, -0.53, 6.36]]
    B = [-4.17, -3.24, 34.89, 1.37]
    eps = 0.0001
    res = iteration(A, B, find_diagonal_preference(A))
    for _ in res:
        print(format(_, ',.4f'), end='  ')