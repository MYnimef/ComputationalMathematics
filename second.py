import random

import numpy as np
from sympy import *
import matplotlib.pyplot as plt


def lagrange():
    length = 5
    n_arr = [i for i in range(0, length)]
    x_arr = [i for i in n_arr]
    y_arr = [random.randint(0, length + i) for i in n_arr]

    print('N = {}'.format(n_arr))
    print('x = {}'.format(x_arr))
    print('y = {}'.format(y_arr))

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

    x_new_arr = [i for i in np.arange(0, length - 0.95, 0.05)]
    y_new_arr = []

    for i in x_new_arr:
        x = i
        y_new_arr.append(eval(p))

    plt.plot(x_new_arr, y_new_arr)
    plt.plot(x_arr, y_arr, 'ro')
    plt.show()
