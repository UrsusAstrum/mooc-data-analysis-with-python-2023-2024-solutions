#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    cos = np.sum(X * Y, axis=1) / (scipy.linalg.norm(X, axis=1) * scipy.linalg.norm(Y, axis=1))

    return np.rad2deg(np.arccos(np.clip(cos, a_min=-1, a_max=1)))

def main():
    X = np.array([[1, 2], [1, 2]])
    Y = np.array([[3, 4], [3, 4]])
    print(X * Y)
    print(vector_angles(X, Y))

if __name__ == "__main__":
    main()
