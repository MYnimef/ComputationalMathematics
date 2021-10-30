import random
from sympy import *


class IntegralCalculator:
    def __init__(self, k=random.randint(20, 50) / 10, l=random.randint(1, 50) / 10):
        self.k = k
        self.l = l

        self.a = (k - l) / 2
        self.b = k + l
        x = symbols('x')
        self.fx = str((x + l) / (x**2 + x + k))
        self.n = [4, 6, 8]

        self.calculate()

    def __f(self, x) -> float:
        return eval(self.fx, {'x': x})

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
            print('{}'.format(self.trap(i)))

    def parabola(self, n):
        pass

    def calculate_parabola(self):
        print('Метод парабол:')
        for i in self.n:
            print('{}'.format(self.parabola(i)))

    def gauss(self, n):
        pass

    def calculate_gauss(self):
        print('Метод Гаусса:')
        for i in self.n:
            print('{}'.format(self.gauss(i)))

    def calculate(self):
        print('Подытегральное выражение {} , пределы интегрирования a = {}, b = {}'
              .format(self.fx, self.a, self.b))
        self.calculate_trap()
        self.calculate_parabola()
        self.calculate_gauss()

IntegralCalculator(4, 2)
