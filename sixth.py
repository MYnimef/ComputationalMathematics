import numpy as np
from matplotlib import pyplot as plt
from sympy import *


def calculate(equation, i) -> float:
    x = i
    return eval(result)


if __name__ == '__main__':
    # Ввод исходных данных
    K = 3
    L = 2

    # Инициализация исходного дифференциального уравнения
    x = Symbol('x')
    f = symbols('f', cls=Function)
    diffEq = Eq(f(x).diff(x), x ** 2 + (K - 1) / 2 * f(x))
    print('{}'.format(diffEq))

    # Решение дифференциального уравнения
    result = str(dsolve(diffEq, f(x), ics={f(0): L}))
    result = result.replace('Eq(f(x), ', '')
    result = result.removesuffix(')')

    # Построение графика
    size = 2
    h = 0.05
    x_arr = [i for i in np.arange(0, size, h)]
    y_arr = [calculate(result, i) for i in np.arange(0, size, h)]
    plt.plot(x_arr, y_arr)
    plt.show()

    # Красивый вывод ответа
    result = result.replace('**', '^')
    print('f(x) = {}'.format(result))
