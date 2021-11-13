import first
from second import Interpolation
from fourth import IntegralCalculator
from third import RootFinder

if __name__ == '__main__':
    print('\nПервое занятие\n')

    print('\n____________________\n')
    first.first_task()
    print('\n____________________\n')
    first.second_task()
    print('\n____________________\n')
    first.third_task()
    print('\n____________________\n')

    print('\nВторое занятие\n')

    interpolation = Interpolation()
    interpolation.lagrange()
    interpolation.first_newton()

    print('\nТретье занятие\n')
    rt = RootFinder()
    rt.calculate()

    print('\nЧетвертое занятие\n')
    ig = IntegralCalculator()
