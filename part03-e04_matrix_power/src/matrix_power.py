#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0])
    if n < 0:
         a = np.linalg.inv(a)
         n = -1 * n

    return reduce(lambda x, y: x @ y, (a for i in range(n)))

def main():
    return

if __name__ == "__main__":
    main()
