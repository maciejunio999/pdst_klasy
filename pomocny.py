import numpy
from math import pi

m, n = 10, 10

for i in range(m):
    for j in range(n):
        print('*' if i in [0, n-1] or j in [0, m-1] else ' ', end='')
    print()

a = 1
b = 2
print(numpy.arcsin(a/b))
print(pi/6)

