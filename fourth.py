import math
import random

from sympy import *


class IntegralCalculator:
    def __init__(self, k=random.randint(20, 50) / 10, l=random.randint(1, 50) / 10):
        self.k = k
        self.l = l

        self.a = (k - l) / 2
        self.b = k + l
        x = symbols('x')
        self.fx = (x + l) / (x ** 2 + x + k)
        self.n = [4, 6, 8]

        self.calculate()

    def __f(self, x) -> float:
        return self.fx.subs({'x': x})

    def trap(self, n):
        f = self.__f
        a = self.a
        b = self.b

        del_x = (b - a) / n
        result = (f(b) + f(a)) / 2
        for i in range(1, n):
            result += f(a + del_x * i)
        return result * del_x

    def calculate_trap(self):
        print('Метод трапеций:')
        for i in self.n:
            print('n = {} , результат: {}'.format(i, self.trap(i)))

    def parabola(self, n):
        N = 2 * n
        f = self.__f
        left = self.a
        right = self.b
        h = (right - left) / N

        result = 0
        for step in range(1, N, 2):
            result += f(left + (step - 1) * h) + 4 * f(left + step * h) + f(left + (step + 1) * h)
        return (h / 3) * result

    def calculate_parabola(self):
        print('Метод парабол:')
        for i in self.n:
            print('n = {} , результат: {}'.format(i, self.parabola(i)))

    def gauss(self, n):
        a = self.a
        b = self.b

        del_x = (b - a) / n
        result = 0
        for i in range(0, n):
            beginning = a + i * del_x
            result += self.__gauss_iter(beginning, beginning + del_x)

        return result

    def __gauss_iter(self, a, b):
        f = self.__f
        first = (a + b) / 2
        second = (b - a) / (2 * 3 ** (1 / 2))
        return (b - a) / 2 * (f(first - second) + f((first + second)))

    def calculate_gauss(self):
        print('Метод Гаусса:')
        for i in self.n:
            print('n = {} , результат: {}'.format(i, self.gauss(i)))

    def calculate(self):
        print('Подытегральное выражение {} , пределы интегрирования a = {}, b = {}'
              .format(self.fx, self.a, self.b))
        self.calculate_trap()
        self.calculate_parabola()
        self.calculate_gauss()

    def accurate(self):
        return self.__accurate_func(self.b) - self.__accurate_func(self.a)

    def __accurate_func(self, x):
        k = self.k
        l = self.l
        return 1 / 2 * math.log(x ** 2 + x + k) + (l - 1 / 2) / ((k - 1 / 4) ** (1 / 2)) * math.atan(
            (x + 1 / 2) / ((k - 1 / 4) ** (1 / 2)))


if __name__ == '__main__':
    ig = IntegralCalculator()
    # ig = IntegralCalculator(2.6, 1.6)  # 8
    # ig = IntegralCalculator(2.2, 1.2)  # 6
    print('Точное значение = {}'.format(ig.accurate()))
