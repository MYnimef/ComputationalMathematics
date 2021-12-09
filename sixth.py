from matplotlib import pyplot as plt
from sympy import *

if __name__ == '__main__':
    x = Symbol('x')
    f = symbols('f', cls=Function)

    K = 3
    L = 2

    diffeq = Eq(f(x).diff(x), x ** 2 + (K - 1) / 2 * f(x))
    result = str(dsolve(diffeq, f(x), ics={f(0): L}))

    result = result.replace('Eq(f(x), ', '')
    result = result.removesuffix(')')

    size = 20
    x_arr = [i for i in range(0, size)]
    y_arr = []
    for i in range(0, size):
        x = i
        y_arr.append(eval(result))

    plt.plot(x_arr, y_arr)
    plt.show()

    result = result.replace('**', '^')
    print('f(x) = {}'.format(result))
