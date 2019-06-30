"""Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do in 0(1) timing."""

from math import hypot as h


a1 = int(input("input first tochka of number x: "))
a2 = int(input("Input second tochka of number x: "))

b1 = int(input("input first tochka of number y: "))
b2 = int(input("Input second tochka of number y: "))


res = round(float(h(b1-a1, b2-a2)), 2)
def distance(a1, a2, b1, b2):
    res = round(float(h(b1-a1, b2-b1)),2)
    return res
print(res)