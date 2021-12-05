import random
from sympy import *


class RootFinder:
    def __init__(self, k=random.randint(20, 50) / 10, l=random.randint(1, 50) / 10, eps=1e-15):
        self.__start(k, l, eps)

    def __start(self, k=random.randint(20, 50) / 10, l=random.randint(1, 50) / 10, eps=1e-15):
        # K SHOULD BE BIGGER THAN L
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
        extreme1 = -self.newton(-1e2, 0)
        extreme2 = self.newton(0, 1e2)
        return [self.newton(-1e2, extreme1), self.newton(extreme1, extreme2), self.newton(extreme2, 1e2)]

    def secant(self, x0, x1):
        f = self.__f

        x2 = 0
        while abs(x1 - x0) > self.eps:
            x2 = x1 - f(x1) * (x1 - x0) / float(f(x1) - f(x0))
            x0, x1 = x1, x2
        return x2

    def calculate_secant(self):
        extreme1 = -self.secant(-1e2, 0)
        extreme2 = self.secant(0, 1e2)
        return [self.secant(-1e2, extreme1), self.secant(extreme1, extreme2), self.secant(extreme2, 1e2)]

    def simple_iterations(self, a):
        k = self.k
        l = self.l

        xn = a
        xn1 = pow(abs(k * xn - l), 1/3)
        while abs(xn1 - xn) > self.eps:
            xn = xn1
            xn1 = pow(abs(k * xn - l), 1/3)
        return xn1

    def calculate_simple_iterations(self):
        return [self.simple_iterations(3), self.simple_iterations(-5), self.simple_iterations(-1e3)]

    @staticmethod
    def print_res(x, name):
        print('\n{}'.format(name))
        for i in range(0, len(x)):
            print('x{} = {}'.format(i + 1, x[i]))

    def calculate(self):
        x = self.calculate_newton()
        result = []
        for i in range(0, len(x)):
            flag = True
            for j in range(0, len(result)):
                num1 = int(x[i] * 1000)
                num2 = int(result[j] * 1000)
                if i != j and num1 == num2:
                    flag = False
                    break
            if flag:
                result.append(x[i])

        if len(result) == 3:
            print('Исходное выражение {} = 0'.format(self.fx).replace('**', '^'))
            self.print_res(result, 'Корни уравнения:')
        elif len(result) == 2:
            sup = self.calculate_secant()
            for i in sup:
                flag = True
                for j in x:
                    if i == j:
                        flag = False
                if flag:
                    result.append(i)
                    print('Исходное выражение {} = 0'.format(self.fx).replace('**', '^'))
                    self.print_res(result, 'Корни уравнения:')
                    break
        else:
            self.__start()
            self.calculate()

    def calculate_all(self):
        print('Исходное выражение {} = 0'.format(self.fx.replace('**', '^')))
        self.print_res(self.calculate_newton(), 'Метод касательных: ')
        self.print_res(self.calculate_secant(), 'Метод хорд:')
        self.print_res(self.calculate_simple_iterations(), 'Метод простых итераций:')


if __name__ == '__main__':
    # rt = RootFinder()
    rt = RootFinder(4.9, 2.3)
    # rt = RootFinder(2.5, 0.8)  # 8
    # rt = RootFinder(3.8, 1.6)  # 6
    # rt = RootFinder(3.9, 2.3)  # 10
    rt.calculate()
