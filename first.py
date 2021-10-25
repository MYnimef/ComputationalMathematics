import math
import random
from sympy import *


def first_task():
    number = random.randint(int(1e4), int(1e5)) / pow(10, random.randint(1, 3))
    epsilon = random.randint(1, 9) / pow(10, random.randint(0, 3))
    print('Задание - Дано приближенное число {}, погрешность - {}. Найти число верных знаков.'
          .format(number, epsilon))

    m = 0
    while number / pow(10, m) >= 10:
        m += 1

    n = 0
    while epsilon <= 0.5 * pow(10, m - n + 1):
        n += 1
    print('Ответ: Кол-во верных знаков = {}.'
          .format(n - 1))


def second_task():
    num = random.randint(0, 4)
    if num == 0:
        trapeze()
    elif num == 1:
        pyramid()
    elif num == 2:
        cone()
    elif num == 3:
        parallelepiped()
    elif num == 4:
        cylinder()


def trapeze():
    beginning = random.randint(2, 8)
    a = beginning * 5
    b = random.randint(beginning + 2, 18) * 5
    h = random.randint(2, 20) * 5
    print('Задание - Равнобедренная трапеция со сторонами основания, равными {} и {} см, и высотой, равной {} см.'
          .format(a, b, h))

    s = (a + b) / 2 * h
    abs_s = h + (a + b) / 2
    rel_s = (abs_s / s) * 100
    print('Ответ: Площадь фигуры = {} +- {} см^2, относительная погрешность = {} %'
          .format(round(s, 3), round(abs_s, 3), round(rel_s, 3)))

    p = 2 * math.sqrt(h ** 2 + ((b - a) / 2) ** 2) + a + b
    abs_p = 4 * h / math.sqrt(4 * h ** 2 + b ** 2 - 2 * a * b + a ** 2) + \
            (a - b + 2) / math.sqrt(4 * h ** 2 + b ** 2 - 2 * a * b + a ** 2 + 4 * (a + b)) * 2
    rel_p = (abs_p / p) * 100
    print('Периметр = {} +- {} см, относительная погрешность = {} %'
          .format(round(p, 3), round(abs_p, 3), round(rel_p, 3)))


def pyramid():
    a = random.randint(2, 30) * 5
    h = random.randint(2, 20) * 5
    print('Задание - Правильная четырехугольная пирамида со стороной основания, равной {} см, и высотой, равной {} см.'
          .format(a, h))

    v = 1 / 3 * a ** 2 * h
    abs_v = 1 / 3 * a * (2 * h + a)
    rel_v = (abs_v / v) * 100
    print('Ответ: Обьем фигуры = {} +- {} см^3, относительная погрешность вычисления = {} %'
          .format(round(v, 3), round(abs_v, 3), round(rel_v, 3)))

    sup = math.sqrt(4 * h ** 2 + a ** 2)
    s = 2 * a * sup + a ** 2
    abs_s = 2 * sup + 2 * a ** 2 / sup + 2 * a + 8 * a * h / sup
    rel_s = (abs_s / s) * 100
    print('Площадь поверхности фигуры = {} +- {} см^2, относительная погрешность вычисления = {} %'
          .format(round(s, 3), round(abs_s, 3), round(rel_s, 3)))


def cone():
    h = random.randint(2, 10) * 5
    r = random.randint(1, 10) * 5
    print('Задание - Конус с высотой, равной {} см, и радиусом, равным {} см.'
          .format(h, r))

    v = 1 / 3 * math.pi * r ** 2 * h
    abs_v = 1 / 3 * math.pi * r * (r + 2 * h)
    rel_v = (abs_v / v) * 100
    print('Ответ: Обьем фигуры = {} +- {} см^3, относительная погрешность вычисления = {} %'
          .format(round(v, 3), round(abs_v, 3), round(rel_v, 3)))

    sup = math.sqrt(h ** 2 + r ** 2)
    s = math.pi * r * (sup + r)
    abs_s = math.pi * sup + math.pi * r ** 2 / sup + math.pi * h * r / sup
    rel_s = (abs_s / s) * 100
    print('Площадь поверхности фигуры = {} +- {} см^2, относительная погрешность вычисления = {} %'
          .format(round(s, 3), round(abs_s, 3), round(rel_s, 3)))


def parallelepiped():
    h = random.randint(4, 20) * 5
    beginning = random.randint(4, 20)
    a = beginning * 5
    d = random.randint(beginning + 2, 30) * 5
    print('Задание - Прямоугольный параллелепипед с высотой {} см, стороной основания {} см и диагональю основания {} '
          'см. '
          .format(h, a, d))

    sup = math.sqrt(d ** 2 - a ** 2)

    v = a * sup * h
    abs_v = sup * h - a ** 2 / sup * h + a * d / sup * h + a * sup
    rel_v = (abs_v / v) * 100
    print('Ответ: Обьем фигуры = {} +- {} см^3, относительная погрешность вычисления = {} %'
          .format(round(v, 3), round(abs_v, 3), round(rel_v, 3)))

    s = 2 * ((a + h) * sup + a * h)
    abs_s = 2 * (sup - a ** 2 / sup - a * h / sup + h + (a + h) * d / sup + sup + a)
    rel_s = (abs_s / s) * 100
    print('Площадь поверхности фигуры = {} +- {} см^2, относительная погрешность вычисления = {} %'
          .format(round(s, 3), round(abs_s, 3), round(rel_s, 3)))


def cylinder():
    h = random.randint(4, 20) * 5
    d = random.randint(4, 20) * 5
    print('Задание - Цилиндр с образующей, равной {} см, и главной диагональю, равной {} см.'
          .format(h, d))

    v = (math.pi * (d ** 2) * h) / 4
    abs_v = (math.pi * d * h) / 2 + (math.pi * (d ** 2)) / 4
    rel_v = (abs_v / v) * 100
    print('Ответ: Обьем фигуры = {} +- {} см^3, относительная погрешность вычисления = {} %'
          .format(round(v, 3), round(abs_v, 3), round(rel_v, 3)))

    s = 2 * math.pi * (d / 2) * (d / 2 + h)
    abs_s = math.pi * (3 * d + h)
    rel_s = (abs_s / s) * 100
    print('Площадь поверхности фигуры = {} +- {} см^2, относительная погрешность вычисления = {} %'
          .format(round(s, 3), round(abs_s, 3), round(rel_s, 3)))


def third_task():
    postfix = ''

    """
    postfix = ''
    operators = []

    for symbol in infix:
        if symbol.isalpha():
            postfix += symbol
        elif symbol == '(':
            operators.append(symbol)
        elif symbol == ')':
            while operators[-1] != '(':
                postfix += operators.pop()
            operators.pop()
        elif symbol != ' ':
            while operators and not(operators[-1] == '(') and priority(symbol) <= priority(operators[-1]):
                postfix += operators.pop()
            operators.append(symbol)

    while operators:
        postfix += operators.pop()
    """

    operand = 0
    for i in range(0, 5):
        sup = random.randint(1, 3)
        while operand == sup:
            sup = random.randint(1, 3)
        operand = sup

        if operand == 1:
            postfix += 'x'
        elif operand == 2:
            postfix += 'y'
        elif operand == 3:
            postfix += 'z'

        step = random.randint(0, 2)
        if step == 1:
            postfix += 'a' + '^'
        elif step == 2:
            postfix += 'b' + '^'

        if i == 1 or i == 3 or i == 4:
            operation = random.randint(1, 4)
            if operation == 1:
                postfix += '+'
            elif operation == 2:
                postfix += '-'
            elif operation == 3:
                postfix += '*'
            elif operation == 4:
                postfix += '/'

        if i == 4:
            operation = random.randint(1, 4)
            if operation == 1:
                postfix += '+'
            elif operation == 2:
                postfix += '-'
            elif operation == 3:
                postfix += '*'
            elif operation == 4:
                postfix += '/'

    infix = get_infix(postfix)
    print('Исходная функция = {}'
          .format(infix))
    infix = infix.replace('^', '**')

    x, y, z, a, b = symbols('x y z a b')
    denominator = random.randint(2, 5)
    while denominator == 3:
        denominator = random.randint(2, 5)
    a = 1 / denominator
    b = random.randint(2, 4)
    print('Степени чисел a = {}, b = {}'.format(a, b))

    dx = eval(str(diff(infix, x)))
    dx_str = (str(dx)).replace('**', '^')
    dy = eval(str(diff(infix, y)))
    dy_str = (str(dy)).replace('**', '^')
    dz = eval(str(diff(infix, z)))
    dz_str = (str(dz)).replace('**', '^')
    print('Абсолютная погрешность функции = [{}] * del1 + [{}] * del2 + [{}] * del3'
          .format(dx_str, dy_str, dz_str))

    dx = eval('{} / {}'.format(dx, infix))
    dx_str = (str(dx)).replace('**', '^')
    dy = eval('{} / {}'.format(dy, infix))
    dy_str = (str(dy)).replace('**', '^')
    dz = eval('{} / {}'.format(dz, infix))
    dz_str = (str(dz)).replace('**', '^')
    print('Относительная погрешность функции = [{}] * del1 + [{}] * del2 + [{}] * del3'
          .format(dx_str, dy_str, dz_str))


def get_infix(postfix):
    stack = []
    for i in range(len(postfix)):
        if postfix[i].isalpha():
            stack.append(postfix[i])
        else:
            operator1 = stack.pop()
            operator2 = stack.pop()
            stack.append("(" + operator2 + postfix[i] + operator1 + ")")
    return stack.pop()


def priority(x):
    if x == '+' or x == '-':
        return 1
    return 2
