#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    res = []
    n_rows = a.shape[0]

    for i in range(n_rows):
        res.append(a[i, :])

    return res

def get_columns(a):
    res = []
    n_cols = a.shape[1]

    for i in range(n_cols):
        res.append(a[:, i])

    return res

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
