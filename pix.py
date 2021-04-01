#!/usr/bin/env python3
import numpy as np


n = 1000
assert n % 2 == 0

# x^2 + (y - n//2)^2 = (n/2)^2

A = np.zeros(shape=(n//2, n//2), dtype=np.int8)

for i in range(n//2):
    for j in range(n//2):
        if i**2 + j**2 - (n//2)**2 <= 1:
            A[i, j] = 1

#   print(A)
#   print(A.sum(axis=0))

z = 0
for i in range(n//2 - 1, 0, -1):
    z = sum(A[i, :])
    if z - 1 >= i:
        break
# print(z)
C = 4 * 2 * (z - 1)
print(f'{n=}\t{C/n}')

print(2*2**0.5)
