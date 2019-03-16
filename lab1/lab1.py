import matplotlib.pyplot as plot
import numpy as np
from numpy import mean, var, std

n = int(input("Введите количество случайных чисел, которые вы хотите получить: "))
while True:
    R = int(input("Введите R0: "))
    if R < ((2 ** n) - 1):
        break

a = int(input("Введите a: "))

while True:
    m = int(input("Введите m: "))
    if m > a:
        break

x = []

i = 0
while i < n:
    R = (a * R) % m
    x.insert(i, round(R / m, 4))
    i += 1

x_v = x[len(x) - 1]
# Нахождение периода
i = 0
i1 = -1
i2 = -1
f = 0
while i < len(x):
    if x[i] == x_v:
        if f == 0:
            f = 1
            i1 = i
            i += 1
            continue
        else:
            i2 = i
            break
    i += 1

# Период
P = i2 - i1

# Нахождение длины участка апериодичности
i3 = 0
while x[i3] != x[i3 + P]:
    i3 += 1
L = i3 + P

r_var = max(x) - min(x)
# k - number of intervals
k = 20
delta = round(r_var / k, 2)

mx = mean(x)  # мат. ожидание
mv = var(x)  # дисперсия
ms = std(x)  # СКО

print("Случайные величины: ", x)
print("Период: ", P)
print("Длина участка апериодичности: ", L)
print("Математичсекое ожидание: ", mx)
print("Дисперсия: ", mv)
print("СКО: ", ms)

plot.hist(x)
plot.xticks(np.arange(min(x), max(x), delta))
plot.show()
