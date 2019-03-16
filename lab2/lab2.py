import math

import numpy as np
import pylab
from numpy import mean, var, std

from lehmer import lehmer


# Равномерное распределение
def uniform(a, b, n):
    numbers = lehmer(n)
    for num in numbers:
        num = (a + (b - a) * num)
    return numbers


def uniform_d():
    low = float(input("Введите нижнюю границу для равномерного распереления: "))
    high = float(input("Введите верхнюю границу для равномерного распределения: "))
    size = int(input("Введите количество случайных чисел, которые вы хотите получить: "))
    uniformd = uniform(low, high, size)
    uniform_m = mean(uniformd)
    uniform_v = var(uniformd)
    uniform_s = std(uniformd)
    pylab.hist(uniformd, bins=200, density=True)
    pylab.title("Равномерное распределение")
    print("Равномерное распределение:")
    print("Мат. ожидание: ", uniform_m)
    print("Дисперсия: ", uniform_v)
    print("СКО: ", uniform_s)


# Гауссовское распределение
def normal(size):
    numbers = lehmer(size)
    array = []
    i = 0
    while i < size - 1:
        v1 = -1 + 2 * numbers[i]
        i += 1
        v2 = -1 + 2 * numbers[i]
        s = v1 ** 2 + v2 ** 2
        if s >= 1:
            i += 1
            continue
        if s < 1:
            t1 = v1 * (math.sqrt(-2 * math.log(s) / s))
            t2 = v2 * (math.sqrt(-2 * math.log(s) / s))
            array.append(t1)
            array.append(t2)
            i += 1
    return array


def normal_d():
    size = int(input("Введите количество случайных чисел, которые вы хотите получить: "))
    normald = normal(size)
    normal_m = mean(normald)
    normal_v = var(normald)
    normal_s = std(normald)
    pylab.hist(normald, bins=200, density=True)
    pylab.title("Гауссовское распределение")
    print("Гауссовское (нормальное) распределение:")
    print("Мат. ожидание: ", normal_m)
    print("Дисперсия: ", normal_v)
    print("СКО: ", normal_s)


# Экспоненциальное распределение
def exponential(scale, size):
    numbers = lehmer(size)
    array = []
    for num in numbers:
        array.append(((-1) / scale) * (math.log(1 - num)))
    return array


def exponential_d():
    scale = float(input("Введите параметр L для экспоненциального распределения: "))
    size = int(input("Введите количество случайных чисел, которые вы хотите получить: "))
    exp = exponential(scale, size)
    exp_m = mean(exp)
    exp_v = var(exp)
    exp_s = std(exp)
    pylab.hist(exp, bins=200, density=True)
    pylab.title("Экспоненциальное распределение:")
    print("Экспоненциальное распределение:")
    print("Мат. ожидание: ", exp_m)
    print("Дисперсия: ", exp_v)
    print("СКО: ", exp_s)


# Гамма-распределение
def gamma(nu, l, n):
    numbers = lehmer(n)
    nu = int(nu)
    array = []
    i = 0
    while i < len(numbers):
        array.append((-1 / l) * math.log(gamma_mul(i, nu, numbers, n)))
        i += 1

    return array


def gamma_mul(i, nu, numbers, n):
    mul = 1
    j = i
    while j <= i + nu:
        if j < n:
            mul *= numbers[j]
            j += 1
        else:
            return mul
    return mul


def gamma_d():
    shape = float(input("Введите n для гамма-распределения: "))
    scale = float(input("Введите L для гамма-распределения: "))
    size = int(input("Введите количество случайных чисел, которые вы хотите получить: "))
    gammad = gamma(shape, scale, size)
    gamma_m = mean(gammad)
    gamma_v = var(gammad)
    gamma_s = std(gammad)
    pylab.hist(gammad, bins=200, density=True)
    pylab.title("Гамма-распределение")
    print("Гамма-распределение:")
    print("Мат. ожидание: ", gamma_m)
    print("Дисперсия: ", gamma_v)
    print("СКО: ", gamma_s)


# Треугольое распределение
def triangular(a, b, size):
    numbers = lehmer(size)
    array = []
    for i in np.arange(0, len(numbers) - 1):
        array.append(a + (b - a) * min(numbers[i], numbers[i + 1]))
        i += 2
    return array


def triangular_d():
    left = float(input("Введите левую границу для треугольного распределения: "))
    right = float(input("Введите правую границу для треугольного распределния: "))
    size = int(input("Введите количество случайных чисел, которые вы хотите получить: "))
    tle = triangular(left, right, size)
    tle_m = mean(tle)
    tle_v = var(tle)
    tle_s = std(tle)
    pylab.hist(tle, bins=200, density=True)
    pylab.title("Треугольное распределение")
    print("Треугольное распределение:")
    print("Мат. ожидание: ", tle_m)
    print("Дисперсия: ", tle_v)
    print("СКО: ", tle_s)


# Распределение Симпсона
def simpson(left, right, size):
    numbers = lehmer(size * 2)
    a = left / 2
    b = right / 2
    x = []
    i = 0
    while i < len(numbers):
        y = a + (b - a) * numbers[i]
        z = a + (b - a) * numbers[i + 1]
        x.append(y + z)
        i += 2
    return x


def simpson_d():
    left = float(input("Введите левую границу для распределения Симпсона: "))
    right = float(input("Введите правую границу для распределния Симпсона: "))
    size = int(input("Введите количество случайных чисел, которые вы хотите получить: "))

    simpsond = simpson(left, right, size)
    simpson_m = mean(simpsond)
    simpson_v = var(simpsond)
    simpson_s = std(simpsond)
    pylab.hist(simpsond, bins=200, density=True)
    pylab.title("Распределение Симпсона")
    print("Распределение Симпсона:")
    print("Мат. ожидание: ", simpson_m)
    print("Дисперсия: ", simpson_v)
    print("СКО: ", simpson_s)


def menu(chosen):
    if chosen == 1:
        normal_d()
        pylab.show()
        return
    if chosen == 2:
        uniform_d()
        pylab.show()
        return
    if chosen == 3:
        exponential_d()
        pylab.show()
        return
    if chosen == 4:
        gamma_d()
        pylab.show()
        return
    if chosen == 5:
        triangular_d()
        pylab.show()
        return
    if chosen == 6:
        simpson_d()
        pylab.show()
        return


while True:
    print("Выберите интересующее вас распределение:")
    print("1. Нормальное распределение")
    print("2. Равномерное распределение")
    print("3. Экспоненциальное распределение")
    print("4. Гамма-распределение")
    print("5. Треугольное распределение")
    print("6. Распределение Симпсона")
    print("0. Выход")
    print("")
    number = int(input())
    if number == 0:
        break
    if number < 0 or number > 6:
        print("Такого пункта меню нет. Попробуйте ещё раз. ")
        continue
    else:
        menu(number)
