import math
def f(x):
    return math.log(x) + 2 * (x**2) - 6
a = 1
b = 7
e = 0.01
while (abs(a-b) > e):
    c = (a+b)/2
    if f(c) * f(b) < 0:
        a = c
    else:
        b = c
print(c)