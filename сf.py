class NFException(Exception):
    pass


class CommonFraction:
    """Класс обыкновенной дроби"""

    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise NFException()
        else:
            self.__numerator = numerator
            self.__denominator = denominator
            self.__reduce()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __add__(self, cf):
        self.__numerator = self.__numerator * cf.denominator + cf.numerator * self.__denominator
        self.__denominator *= cf.denominator
        self.__reduce()
        return self

    def __sub__(self, cf):
        self.__numerator = self.__numerator * cf.denominator - cf.numerator * self.__denominator
        self.__denominator *= cf.denominator
        self.__reduce()
        return self

    def __mul__(self, cf):
        self.__numerator *= cf.numerator
        self.__denominator *= cf.denominator
        self.__reduce()
        return self

    def __truediv__(self, cf):
        self.__numerator *= cf.denominator
        self.__denominator *= cf.numerator
        return self

    def __pow__(self, power, modulo=None):
        self.__numerator **= power
        self.__denominator **= power
        self.__reduce()
        return self

    def __float__(self):
        return self.__numerator / self.__denominator

    def __str__(self):
        return "The value is {}/{}".format(self.__numerator, self.__denominator)

    def __get_gcd(self, a, b):
        return a if b == 0 else self.__get_gcd(b, a % b)

    def __reduce(self):
        t = self.__get_gcd(self.__numerator, self.__denominator)
        self.__numerator /= t
        self.__denominator /= t