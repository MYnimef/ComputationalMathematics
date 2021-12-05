from sympy import *

if __name__ == '__main__':
    init_printing()
    # Определить символические константы x и f (x)
    x = Symbol('x')
    f = symbols('f', cls=Function)
    # Используйте команду diffeq для представления дифференциального уравнения: f '' (x) + 3f '(x) + 2f (x) = exp (-x)
    diffeq = Eq(f(x).diff(x, x) + 3 * f(x).diff(x) + 2 * f(x), exp(-x))
    # Вызов функции dsolve, возврат объекта Eq, точность управления подсказкой
    print(dsolve(diffeq, f(x)))
