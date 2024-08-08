#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    a = a ** 2
    a = a.sum(axis=1)
    a = np.sqrt(a)
    return a

def main():
    a = np.array([[3, 4, 5], [1, 2, 3], [10, 10, 10]])
    print(vector_lengths(a))

if __name__ == "__main__":
    main()
