from collections import defaultdict
import bisect
import math
import copy


class Dot:
    def __init__(self, x, y):
        self.x, self.y = [x, y]


class Tuple:
    def __init__(self):
        pass

    a, b, c, d, x = [0.0, 0.0, 0.0, 0.0, 0.0]


def drange(start, stop, step):
    while start < stop:
        yield start
        start += step


def buildSpline(dots):
    for i in range(len(dots)):
        splines[i].x, splines[i].a = dots[i].x, dots[i].y
    alpha, beta = [defaultdict(lambda: 0.), defaultdict(lambda: 0.)]
    for i in range(1, len(dots) - 1):
        c =4. * in_step
        f = 6. * ((dots[i + 1].y - dots[i].y) / in_step - (dots[i].y - dots[i - 1].y) / in_step)
        z = (in_step * alpha[i - 1] + c)
        alpha[i] = -in_step / z
        beta[i] =(f - in_step * beta[i - 1]) / z
    for i in reversed(range(1, len(dots) - 1)):
        splines[i].c = alpha[i] * splines[i + 1].c + beta[i]
    for i in reversed(range(1, len(dots))):
        hi =dots[i].x - dots[i - 1].x
        splines[i].d = (splines[i].c - splines[i - 1].c) / hi
        splines[i].b = hi * (2.0 * splines[i].c + splines[i - 1].c) / 6.0 + (dots[i].y - dots[i - 1].y) / hi


def calc(x):
    distribution = sorted([t[1].x for t in splines.items()])
    indx = bisect.bisect_left(distribution, x)
    if indx == len(distribution):
        return 0
    dx = x - splines[indx].x
    return splines[indx].a + splines[indx].b * dx + splines[indx].c * dx ** 2 / 2. + splines[indx].d * dx ** 3 / 6.


def find_one_addent(x, y, numb):
    numer = [1]
    fist = 0
    if numb != 0:
        numer.append(- x[0])
    else:
        numer.append(- x[1])
        fist = 1
    for _ in range(len(x)):
        if _ != numb and _ != fist:
            tmpres = copy.deepcopy(numer)
            temp = copy.deepcopy(numer)
            tmpres.append(numer[len(numer) - 1] * (-x[_]))
            for j in range(len(tmpres) - 2):
                if j == 0:
                    tmpres[j + 1] -= x[_]
                else:
                    tmpres[j + 1] -= x[_] * temp[j]
                numer = tmpres
    denom = 0
    for _ in range(len(x)):
        if _ != numb:
            tmp = x[numb] - x[_]
            if denom == 0:
                denom = tmp
            else:
                denom *= tmp
    denom = y[numb] / denom
    for elem in range(len(numer)):
        numer[elem] *= denom
    return numer


def lagrange(x, y):
    res = [0 for _ in range(len(x))]
    for _ in range(len(x)):
        tmp = find_one_addent(x, y, _)
        for i in range(len(tmp)):
            res[i] += tmp[i]
    print(res)
    return res


def value_at_point(arr, x):
    dot = arr[len(arr) - 1]
    arr = arr[::-1]
    tmp = x
    for _ in range(len(arr)):
        if _ > 0:
            dot += (arr[_] * tmp)
            tmp *= x
    return dot


if __name__ == '__main__':
    in_func = lambda x: math.e ** x * x ** 2
    in_min_x = -3
    in_max_x = 4
    in_step = 0.25
    x_ = [-3.0, -2.0, -1.0, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    y_ = [0.44, 0.54, 0.36, 0.0, 0.41, 2.71, 10.0, 29.5, 76.1, 180.0, 405.0, 873.0]
    pol = lagrange(x_, y_)
    print 'lagrange:'
    for _ in drange(-3, 4, 0.5):
        print _, '   ', value_at_point(pol, _)
    print 'spline:'
    splines = defaultdict(lambda: Tuple())
    buildSpline(map(lambda x: Dot(x, in_func(x)), [x for x in drange(-3, 5.5, 0.5)]))
    for x in drange(-3, 4.5, 0.5):
        print str(x) + '    ' + str(calc(x))