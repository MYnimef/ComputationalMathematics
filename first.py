import math
import random


def first_task():
    number = random.randint(int(1e4), int(1e5)) / pow(10, random.randint(1, 3))
    epsilon = random.randint(1, 9) / pow(10, random.randint(0, 3))
    print('Дано приближенное число {}, погрешность - {}. Найти число верных знаков.'
          .format(number, epsilon))

    m = 0
    while number / pow(10, m) >= 10:
        m += 1

    n = 0
    while epsilon <= 0.5 * pow(10, m - n + 1):
        n += 1
    print('Кол-во верных знаков = {}.'
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
    a = random.randint(10, 40)
    b = random.randint(a + 20, 90)
    h = random.randint(10, 100)
    print('Равнобедренная трапеция со сторонами основания, равными {} и {} см, и высотой, равной {} см.'
          .format(a, b, h))

    s = (a + b) / 2 * h
    abs_s = h + (a + b) / 2
    rel_s = (abs_s / s) * 100
    print('Площадь фигуры = {} +- {} см^2, относительная погрешность = {} %'
          .format(s, abs_s, rel_s))

    p = 2 * math.sqrt(h ** 2 + ((b - a) / 2) ** 2) + a + b
    abs_p = 4 * h / math.sqrt(4 * h ** 2 + b ** 2 - 2 * a * b + a ** 2) + \
            (a - b + 2) / math.sqrt(4 * h ** 2 + b ** 2 - 2 * a * b + a ** 2 + 4 * (a + b)) * 2
    rel_p = (abs_p / p) * 100
    print('Периметр = {} +- {} см, относительная погрешность = {} %'
          .format(p, abs_p, rel_p))


def pyramid():
    a = random.randint(10, 150)
    h = random.randint(10, 100)

    print('Правильная четырехугольная пирамида со стороной основания, равной {} см, и высотой, равной {} см.'
          .format(a, h))
    pass


def cone():
    h = random.randint(10, 50)
    r = random.randint(5, 50)

    print('Конус с высотой, равной {} см, и радиусом, равным {} см.'
          .format(h, r))
    pass


def parallelepiped():
    h = random.randint(10, 100)
    a = random.randint(10, 100)
    d = random.randint(10, 100)

    print('Прямоугольный параллелепипед с высотой {} см, стороной основания {} см и диагональю основания {} см.'
          .format(h, a, d))
    pass


def cylinder():
    h = random.randint(10, 100)
    d = random.randint(10, 100)
    print('Цилиндр с образующей, равной {} см, и главной диагональю, равной {} см.'
          .format(h, d))

    v = (math.pi * (d ** 2) * h) / 4
    abs_v = (math.pi * d * h) / 2 + (math.pi * (d ** 2)) / 4
    rel_v = (abs_v / v) * 100
    print('Обьем фигуры = {} +- {} см^3, относительная погрешность вычисления = {} %'
          .format(v, abs_v, rel_v))

    s = 2 * math.pi * (d / 2) * (d / 2 + h)
    abs_s = math.pi * (3 * d + h)
    rel_s = (abs_s / s) * 100
    print('Площадь поверхности фигуры = {} +- {} см^2, относительная погрешность вычисления = {} %'
          .format(s, abs_s, rel_s))


def third_task():
    pass


trapeze()
pyramid()
cone()
parallelepiped()
