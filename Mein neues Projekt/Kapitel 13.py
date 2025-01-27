def verdopple(x):
    #assert type(x) in [int, float]  dieser hier ist zum prüfen, dass x immer eine Zahl sein soll
    return 2 * x

a = verdopple(10)
b = verdopple('1')
c = verdopple([1])
d = verdopple(True)
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

from random import randint

s = [randint(0, 1000000) for i in range(100)]
print(f"s = {s}")
