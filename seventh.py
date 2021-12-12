import sympy as sp

if __name__ == '__main__':
    x, t = sp.symbols('x t')
    u = sp.symbols('u', cls=sp.Function)
    c = 2
    diffEq = sp.Eq(u(x, t).diff(x).diff(x), c * u(x, t).diff(t).diff(t))
    print('{}'.format(diffEq))

    # Решение дифференциального уравнения
    result = str(sp.pdsolve(diffEq, u(x, t)))
