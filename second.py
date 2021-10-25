import math
import random

import numpy as np
from sympy import *
import matplotlib.pyplot as plt


def input_data():
    length = 5
    n_arr = [i for i in range(0, length)]
    x_arr = [i for i in n_arr]
    y_arr = [random.randint(0, length + i) for i in n_arr]

    print('N = {}'.format(n_arr))
    print('x = {}'.format(x_arr))
    print('y = {}'.format(y_arr))

    return [length, n_arr, x_arr, y_arr]


def plot_graphics(length, x_arr, y_arr, p):
    x_new_arr = [i for i in np.arange(0, length - 0.95, 0.05)]
    y_new_arr = []

    for i in x_new_arr:
        x = i
        y_new_arr.append(eval(p))

    plt.plot(x_new_arr, y_new_arr)
    plt.plot(x_arr, y_arr, 'ro')
    plt.show()


def lagrange():
    length, n_arr, x_arr, y_arr = input_data()

    x = symbols('x')
    p = ''
    for i in n_arr:
        drop = ''
        for j in n_arr:
            if i != j:
                drop += '((x - ' + str(x_arr[j]) + ') / (' + str(x_arr[i]) + ' - ' + str(x_arr[j]) + ')) *'
        p += str(y_arr[i]) + ' * ' + drop + ' 1 + '
    p += '0'

    p = str(simplify(p))
    p_str = p.replace('**', '^')
    print('Полином Лагранжа P(x) = {}'.format(p_str))

    plot_graphics(length, x_arr, y_arr, p)


def newton():
    length, n_arr, x_arr, y_arr = input_data()

    x = symbols('x')
    sup_y = y_arr.copy()
    p = str(y_arr[0])
    for i in range(0, length - 1):
        del_y = []
        for j in range(0, length - i - 1):
            del_y.append(sup_y[j + 1] - sup_y[j])
        sup_y = del_y.copy()

        p += ' + (' + str(del_y[0] / (math.factorial(i + 1) * (x_arr[i + 1] - x_arr[i]) ** (i + 1))) + ')'

        for j in range(0, i + 1):
            p += ' * (x - ' + str(x_arr[j]) + ')'

    p = str(simplify(p))
    p_str = p.replace('**', '^')
    print('Полином Ньютона P(x) = {}'.format(p_str))

    plot_graphics(length, x_arr, y_arr, p)
