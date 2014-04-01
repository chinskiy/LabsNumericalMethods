def pol_val(pol, val):
    res = 0
    for i in range(len(pol)):
        res += pol[i] * (val ** i)
    return res


def bisection_meth(a, b, pol, eps):
    i = 0
    while abs(a - b) > eps:
        c = (a + b)/2
        if pol_val(pol, a) * pol_val(pol, c) <= 0:
            b = c
        elif pol_val(pol, b) * pol_val(pol, c) <= 0:
            a = c
        print(i,'  ', c)
        i += 1
    print((a+b)/2)


def xord_meth(a, b, pol, eps):
    c = (a * pol_val(pol, b) - b * pol_val(pol, a)) / (pol_val(pol, b) - pol_val(pol, a))
    c_pr = 0
    i = 0
    while abs(c - c_pr) > eps or pol_val(pol, c) > eps:
        if pol_val(pol, a) * pol_val(pol, c) <= 0:
            b = c
        elif pol_val(pol, b) * pol_val(pol, c) <= 0:
            a = c
        c_pr = c
        print(i,'  ', c)
        i += 1
        c = (a * pol_val(pol, b) - b * pol_val(pol, a)) / (pol_val(pol, b) - pol_val(pol, a))
    print(c)


def derivative(pol):
    pol1 = []
    for i in range(len(pol)):
        pol1.append(pol[i] * i)
    pol1.pop(0)
    return pol1


def newton_meth(x0, pol, eps):
    i = 0
    pol1 = derivative(pol)
    x1 = x0 - pol_val(pol, x0) / pol_val(pol1, x0)
    while abs(x1 - x0) > eps or abs(pol_val(pol, x1)) > eps:
        i += 1
        x0 = x1
        print(i,'  ', x1)
        x1 = x0 - pol_val(pol, x0) / pol_val(pol1, x0)
    print(x1)

if __name__ == "__main__":
    polyn = [1, -3, 1, -2, -4]
    polyn = polyn[::-1]
    eps = 0.00001
    #bisection_meth(-1, -0.25, polyn, eps)
    bisection_meth(2.75, 3.5, polyn, eps)
    #xord_meth(-1, -0.25, polyn, eps)
    #xord_meth(2.75, 3.5, polyn, eps)
    #newton_meth(2.75, polyn, eps)