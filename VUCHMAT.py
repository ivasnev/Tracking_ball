def func(x, k, l):
    return (x + l) / (x * x + x + k)


def gaus_1_4(k, l):
    t_i = [-0.861136, -0.339981, 0.339981, 0.861136]
    a_i = [0.347854, 0.652145, 0.652145, 0.347854]

    sum = 0
    res = 0
    a = (k - l) / 2
    b = k + l
    for i in range(1, 5):
        x = (a + b) / 2 + ((b - a) / 2) * t_i[i - 1]
        f = func(x, k, l)
        tmp = a_i[i - 1] * f
        sum += tmp
        print('{} {:.7f} | {:.7f} '.format(i, x, tmp))
    res = ((b - a) / 2) * sum
    print(res)
    print()


def gaus_1_6(k, l):
    t_i = [-0.932464, -0.661209, -0.238619, 0.238619, 0.661209, 0.932464]
    a_i = [0.171324, 0.360761, 0.467913, 0.467913, 0.360761, 0.171324]

    sum = 0
    res = 0
    a = (k - l) / 2
    b = k + l
    for i in range(1, 7):
        x = (a + b) / 2 + ((b - a) / 2) * t_i[i - 1]
        f = func(x, k, l)
        tmp = a_i[i - 1] * f
        sum += tmp
        print('{} {:.7f} | {:.7f}'.format(i, x, tmp))
    res = ((b - a) / 2) * sum
    print(res)
    print()


def gaus_1_8(k, l):
    t_i = [-0.960289, -0.796666, -0.525532, -0.183434, 0.183434, 0.525532, 0.796666, 0.960289]
    a_i = [0.101228, 0.222381, 0.313706, 0.362683, 0.362683, 0.313706, 0.222381, 0.101228]
    sum = 0
    res = 0
    a = (k - l) / 2
    b = k + l
    for i in range(1, 9):
        x = (a + b) / 2 + ((b - a) / 2) * t_i[i - 1]
        f = func(x, k, l)
        tmp = a_i[i - 1] * f
        sum += tmp
        print('{} {:.7f} | {:.7f}'.format(i, x, tmp))
    res = ((b - a) / 2) * sum
    print(res)
    print()


def trap(k, l, n):
    sum = 0
    res = 0
    a = (k - l) / 2
    b = k + l
    h = (b - a) / n
    res = func(a, k, l) + func(b, k, l)
    for i in range(1, n):
        x = 0.8 + h * i
        f = func(x, k, l)
        res += 2 * f
        print('{} {:.7f} | {:.7f}'.format(i, x, f))
    res = (h / 2) * res
    print(res)
    print()


def func2(x, y):
    return x * x + 1.3 * y


def eler(k, l):
    h = 0.5
    x = 0
    y = l
    for i in range(4):
        y = y + h * func2(x, y)
        x = x + h
        print('{} {}  '.format(x, y))
    print()


def trap2(k, l):
    h = 0.5
    x = [0, 0, 0, 0, 0]
    y = [l, 0, 0, 0, 0]
    for i in range(4):
        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + (h / 2) * (func2(x[i], y[i]) + func2(x[i + 1], y[i] + h * func2(x[i], y[i])))
        y[i + 1] = round(y[i + 1], 3)
        print(x[i], y[i])
    print(x[4], y[4])
    print()


def RK(k, l):
    h = 0.5
    x = [0, 0, 0, 0, 0]
    y = [l, 0, 0, 0, 0]
    for i in range(4):
        x[i + 1] = x[i] + h
        k_1 = round(func2(x[i], y[i]), 3)
        k_2 = round(func2(x[i] + h / 2, y[i] + (h * k_1) / 2), 3)
        k_3 = round(func2(x[i] + h / 2, y[i] + (h * k_2) / 2), 3)
        k_4 = round(func2(x[i] + h, y[i] + (h * k_3)), 3)
        y[i + 1] = round(y[i] + (h / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4), 3)
        print('k1 = {}, k2 = {}, k3 = {}, k4 = {}, y({}) = {},x({}) = {}'.format(k_1, k_2, k_3, k_4,i+1, y[i + 1],i+1, x[i + 1]))


k = 3.6
l = 2.0

eler(k, l)
trap2(k, l)
RK(k, l)
