import first
from second import Interpolation
from fourth import IntegralCalculator
from third import RootFinder


def first_input():
    print('Введи номер: ')
    number = float(input())
    print('Введи погрешность: ')
    eps = float(input())
    first.first_task(number, eps)
    print('\n____________________\n')
    first.second_task()
    print('\n____________________\n')
    first.third_task()


def second_input():
    print('Введи значения x: ')
    x = list(map(int, input().split()))
    print('Введи значения y: ')
    y = list(map(int, input().split()))
    try:
        interpolation = Interpolation(x, y)
        interpolation.lagrange()
        interpolation.first_newton()
    except Exception:
        print('Разное кол-во точек это сильно.')


def third_input():
    print('Введи K: ')
    k = input()
    print('Введи L: ')
    l = input()
    rt = RootFinder(k, l)
    rt.calculate()


def fourth_input():
    print('Введи K: ')
    k = input()
    print('Введи L: ')
    l = input()
    IntegralCalculator(k, l)


if __name__ == '__main__':
    print('Добро пожаловать в PyKaif!\nВведи номер темы, по которой нужно решить задание:')

    while True:
        print('(Для выхода из лупы введи какой-то бред)')
        choice = input()

        if choice == '1':
            first_input()
        elif choice == '2':
            second_input()
        elif choice == '3':
            third_input()
        elif choice == '4':
            fourth_input()
        else:
            break
