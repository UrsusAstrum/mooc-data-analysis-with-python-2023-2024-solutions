#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    indicies = np.array([])
    unique, counts = np.unique(a[:,c], return_counts=True)
    unique = unique[np.argsort(counts)][::-1]
    for val in unique:
        indicies = np.append(indicies, np.where(a[:,c] == val)[0])

    indicies = indicies.astype(int)

    return a[indicies]

def main():
    a = np.array([
        [1, 2, 3],
        [4, 5, 3],
        [6, 2, 1],
        [5, 2, 1],
        [4, 2, 1],
        [1, 1, 0]
    ])

    print(most_frequent_first(a, -1))

if __name__ == "__main__":
    main()
