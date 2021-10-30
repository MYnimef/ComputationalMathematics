import random

from sympy import *


class RootFinder:
    def __init__(self, k=random.randint(20, 50) / 10, l=random.randint(1, 50) / 10, eps=1e-15):
        self.k = k
        self.l = l

        x = symbols('x')
        self.fx = str(x ** 3 - k * x + l)
        self.dfx = str(diff(self.fx, x))
        self.d2fx = str(diff(self.dfx, x))

        self.eps = eps

    def __f(self, x) -> float:
        return eval(self.fx, {'x': x})

    def __df(self, x) -> float:
        return eval(self.dfx, {'x': x})

    def newton(self, a, b):
        f = self.__f
        df = self.__df

        x = (a + b) / 2
        xn = f(x)
        xn1 = xn - f(xn) / df(xn)
        while abs(xn1 - xn) > self.eps:
            xn = xn1
            xn1 -= f(xn) / df(xn)
        return xn1

    def calculate_newton(self):
        extreme1 = -self.newton(-1e3, 0)
        extreme2 = self.newton(0, 1e3)

        print('\nМетод касательных: ')
        print(self.newton(-1e3, extreme1))
        print(self.newton(extreme1, extreme2))
        print(self.newton(extreme2, 1e3))

    def secant(self, x0, x1):
        f = self.__f

        x2 = 0
        while abs(x1 - x0) > self.eps:
            x2 = x1 - f(x1) * (x1 - x0) / float(f(x1) - f(x0))
            x0, x1 = x1, x2
        return x2

    def calculate_secant(self):
        extreme1 = -self.newton(-1e3, 0)
        extreme2 = self.newton(0, 1e3)

        print('\nМетод хорд: ')
        print(self.secant(-1e3, extreme1))
        print(self.secant(extreme1, extreme2))
        print(self.secant(extreme2, 1e3))

    def simple_iterations(self, a):
        xn = pow(self.k * a - self.l, 1 / 3)
        xn1 = xn + 1
        while abs(xn1 - xn) > self.eps:
            xn = xn1
            xn1 = pow(self.k * xn - self.l, 1 / 3)
        return xn1

    def calculate_simple_iterations(self):
        print('\nМетод простых итераций: ')
        print(self.simple_iterations(-1e3))
        print(self.simple_iterations(0))
        print(self.simple_iterations(1e3))

    def calculate(self):
        print('Исходное выражение {} = 0'.format(self.fx))
        self.calculate_newton()
        self.calculate_secant()
        self.calculate_simple_iterations()


rt = RootFinder(20, 10)
rt.calculate()
