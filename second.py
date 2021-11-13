import math
import random

import numpy as np
from sympy import *
import matplotlib.pyplot as plt


class Interpolation:
    def __init__(self, x_arr: list = None, y_arr: list = None):
        if y_arr is None or x_arr is None:
            self.length = 5
            n = range(0, self.length)
            self.den = random.randint(0, 1)
            self.x_arr = [i / pow(2, self.den) for i in n]
            self.y_arr = [random.randint(0, self.length + i) * pow(-1, (random.randint(0, 1))) for i in n]
        elif len(x_arr) != len(y_arr):
            raise Exception('Idiota')
        else:
            self.length = len(x_arr)
            self.den = 1
            self.x_arr = x_arr
            self.y_arr = y_arr

        self.x_arr_int = [int(i * 10) for i in self.x_arr]
        self.y_arr_int = [int(i * 10) for i in self.y_arr]

        print('x = {}'.format(self.x_arr))
        print('y = {}'.format(self.y_arr))

    def __plot_graphics(self, p):
        x_new_arr = [i for i in np.arange(self.x_arr[0], self.x_arr[-1], 0.05 / pow(10, self.den))]
        y_new_arr = []

        for i in x_new_arr:
            x = i
            y_new_arr.append(eval(p))

        plt.plot(x_new_arr, y_new_arr)
        plt.plot(self.x_arr, self.y_arr, 'ro')
        plt.show()

    def __simplify(self, p: str) -> str:
        p = str(simplify(p))
        p = str(expand(p))
        for i in reversed(range(2, self.length)):
            search = 'x**' + str(i)
            if search in p:
                p = p.replace(search, str(pow(10, i - 1)) + '*' + search)
        p += '+1'
        p = str(simplify(p))
        p += '/10 - 1/10'
        return str(simplify(p))

    def lagrange(self):
        x_arr = self.x_arr_int
        y_arr = self.y_arr_int

        x = symbols('x')
        p = ''
        n = range(0, self.length)
        for i in n:
            drop = ''
            for j in n:
                if i != j:
                    drop += '((x-' + str(x_arr[j]) + ')/(' + str(x_arr[i]) + '-' + str(x_arr[j]) + '))*'
            p += str(y_arr[i]) + '*' + drop + '1+'
        p += '0'

        p = self.__simplify(p)

        p_str = p.replace('**', '^')
        print('Полином Лагранжа P(x) = {}'.format(p_str))

        self.__plot_graphics(p)

    def first_newton(self):
        x_arr = self.x_arr_int
        y_arr = self.y_arr_int

        x = symbols('x')
        sup_y = y_arr.copy()
        p = str(y_arr[0])
        for i in range(0, self.length - 1):
            del_y = []
            for j in range(0, self.length - i - 1):
                del_y.append(sup_y[j + 1] - sup_y[j])
            sup_y = del_y.copy()

            p += '+((' + str(del_y[0]) + ')/(' + str(
                math.factorial(i + 1) * (x_arr[i + 1] - x_arr[i]) ** (i + 1)) + '))'

            for j in range(0, i + 1):
                p += '*(x-' + str(x_arr[j]) + ')'

        p = self.__simplify(p)

        p_str = p.replace('**', '^')
        print('Первый полином Ньютона P(x) = {}'.format(p_str))

        self.__plot_graphics(p)


if __name__ == '__main__':
    interpolation = Interpolation()
    # interpolation = Interpolation([0, 0.5, 1, 1.5], [2, -2, -1, 1]) # 8/1
    # interpolation = Interpolation([-0.5, 0, 0.5, 1], [1, 2, -1, -1]) # 9/2
    # interpolation = Interpolation([-1, -0.5, 0, 0.5], [1, -1, 2, 1]) # 10/3
    # interpolation = Interpolation([0, 0.5, 1, 1.5], [1, -1, 2, 1])  # 10/1
    # interpolation = Interpolation([-1, -0.5, 0, 0.5], [-1, -1, 2, -2])  # 11/3
    interpolation.lagrange()
    interpolation.first_newton()
