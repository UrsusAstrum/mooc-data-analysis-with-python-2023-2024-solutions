#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    return ((a.shape[0] - 1) / 2, (a.shape[1] - 1) / 2)

def radial_distance(a):
    res = np.zeros(a.shape[:2])
    mid = center(a)

    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            res[i][j] = np.linalg.norm(mid - np.array([i, j]))
    
    return res

def scale(a, tmin=0.0, tmax=1.0):
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))

def radial_mask(a):
    return scale(1 - radial_distance(a))

def radial_fade(a):
    return a * radial_mask(a)[:, :, np.newaxis]

def main():
    img = plt.imread("src/painting.png")
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(img)
    ax[1].imshow(radial_mask(img))
    ax[2].imshow(radial_fade(img))

    plt.show()

if __name__ == "__main__":
    main()
