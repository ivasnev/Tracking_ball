import math


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
        print('k1 = {}, k2 = {}, k3 = {}, k4 = {}, y({}) = {},x({}) = {}'.format(k_1, k_2, k_3, k_4, i + 1, y[i + 1],
                                                                                 i + 1, x[i + 1]))


def func3(x, a, b):
    return a * x * x * x + a * b * x * x - a * x - b*a


def func3_d(x, a, b):
    return a * 3 * x * x + a * 2 * b * x - a


def SimpIter(a, b):
    counter = 1
    a_g = -4.18
    b_g = -2.267
    arr = [b_g]
    while True:
        print(func3(arr[counter - 1], a, b) * ((b_g - a_g) / (func3(b_g, a, b) - func3(a_g, a, b))))
        arr.append(
            arr[counter - 1] - func3(arr[counter - 1], a, b) * ((b_g - a_g) / (func3(b_g, a, b) - func3(a_g, a, b))))
        t1 = func3(arr[counter] - 10 ** (-3), a, b)
        t2 = func3(arr[counter] + 10 ** (-3), a, b)
        print(counter, ") ", arr[counter], " t1) ", t1, " t2) ", t2)
        if t1 * t2 < 0:
            break
        else:
            counter += 1


def Hord(a, b):
    counter = 1
    a_g = -2.68
    b_g = -0.5
    arr = [a_g]
    while True:
        print(func3(arr[counter - 1], a, b),
              ((b_g - arr[counter - 1]) / (func3(b_g, a, b) - func3(arr[counter - 1], a, b))))
        arr.append(
            arr[counter - 1] - func3(arr[counter - 1], a, b) * (
                    (b_g - arr[counter - 1]) / (func3(b_g, a, b) - func3(arr[counter - 1], a, b))))
        t1 = func3(arr[counter] - 10 ** (-3), a, b)
        t2 = func3(arr[counter] + 10 ** (-3), a, b)
        print(counter, ") ", arr[counter], " t1) ", t1, " t2) ", t2)
        if t1 * t2 < 0:
            break
        else:
            counter += 1


def Kos(a, b):
    counter = 1
    a_g = 0.147
    b_g = 2
    arr = [b_g]
    while True:
        print(func3(arr[counter - 1], a, b), func3_d(arr[counter - 1], a, b))
        arr.append(
            arr[counter - 1] - func3(arr[counter - 1], a, b) / func3_d(arr[counter - 1], a, b))
        t1 = func3(arr[counter] - 10 ** (-3), a, b)
        t2 = func3(arr[counter] + 10 ** (-3), a, b)
        print(counter, ") ", arr[counter], " t1) ", t1, " t2) ", t2)
        if t1 * t2 < 0:
            break
        else:
            counter += 1

# def calc():
#     x = 1 / math.sqrt(2)
#     a = 1 / math.sqrt(2)
#     c = -1 / math.sqrt(2)
#     b = -1 / math.sqrt(2)
#     print(6*x*x - 4*c*x - 4*b*x + 2*b*c -4*a*x + 2*a*c + 2*a*b)
#     print(x*x*x - c*x*x -b*x*x+b*c*x-a*x*x + a*c*x + a*b*x - a*b*c)
#     print((-1*(6*x*x - 4*c*x - 4*b*x + 2*b*c -4*a*x + 2*a*c + 2*a*b))/(x*x*x - c*x*x -b*x*x+b*c*x-a*x*x + a*c*x + a*b*x - a*b*c))
#
# calc()

# a = 1.5
# b = 3.18
# SimpIter(a,b)
# print()
# Hord(a, b)
# print()
# Kos(a, b)
