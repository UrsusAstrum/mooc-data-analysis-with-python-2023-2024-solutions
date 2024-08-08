#!/usr/bin/env python3

import numpy as np

def diamond(n):
    eye = np.eye(n, dtype=int)
    eye_top = np.concatenate((np.flip(eye, axis=1)[:,: n - 1], eye), axis=1)
    eye_tot = np.concatenate((eye_top, np.flip(eye_top)[1:,:]), axis=0)
    return np.array(eye_tot)

def main():
    print(diamond(3))

if __name__ == "__main__":
    main()
