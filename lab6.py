def find_f(x, y):
    return (1 - x ** 2) * y + x * (2 - x + x ** 3)


def runge_kutt(h, left, right):
    x, y = 0, 0
    res = []
    while right >= left:
        res.append(y)
        left += h
        k1 = h * find_f(x, y)
        k2 = h * find_f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * find_f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * find_f(x + h, y + k3)
        y += (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x = left
    res.append(y)
    return res


def adams_bashford(h, left, right):
    tmp = runge_kutt(h, left, right)
    res = [tmp[0], tmp[1], tmp[2], tmp[3]]
    x = left
    i = 3
    while right > x:
        res.append(res[i] + (h / 24) *
                  (55*find_f(x + 3 * h, res[i]) -
                   59*find_f(x + 2 * h, res[i-1]) +
                   37*find_f(x + h, res[i-2]) -
                   9*find_f(x, res[i-3])))
        x += h
        i += 1
    return res


if __name__ == '__main__':
    resrunge = runge_kutt(0.1, 0, 4)
    resadam = adams_bashford(0.1, 0, 4)
    x = 0
    i = 0
    # while x < 3:
    #     q = str(round(x**2, 4))
    #     for _ in range(len(q)):
    #         if q[_] == '.':
    #             q = q[:_] + ',' + q[_+1:]
    #     print(q)
    #     i += 1
    #     x += 0.1

    # while x < 3:
    #     q = str(round(resadam[i], 7))
    #     for _ in range(len(q)):
    #         if q[_] == '.':
    #             q = q[:_] + ',' + q[_+1:]
    #     print(q)
    #     i += 1
    #     x += 0.1

    while x < 4:
        print(round(x, 2), (7 - len(str(round(x, 1)))) * ' ',
              round(x**2, 4), (7 - len(str(round(x**2, 4)))) * ' ',
              round(resrunge[i], 6), (12 - len(str(round(resrunge[i], 6)))) * ' ',
              round(resadam[i], 7))
        i += 1
        x += 0.1
    print(round(x, 1), (7 - len(str(round(x, 1)))) * ' ',
          round(x**2, 4), (7 - len(str(round(x**2, 4)))) * ' ',
          round(resrunge[i], 6), (12 - len(str(round(resrunge[i], 6)))) * ' ',
          round(resadam[i], 7))