#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(img):
    return img[:,:,0] * 0.2126 + img[:,:,1] * 0.7152 + img[:,:,2] * 0.0722

def to_red(img):
    img[:,:,[1, 2]] = 0
    return img

def to_blue(img):
    img[:,:,[0, 1]] = 0
    return img

def to_green(img):
    img[:,:,[0, 2]] = 0
    return img

def main():
    img = plt.imread("src/painting.png")
    plt.gray()
    plt.imshow(to_grayscale(img))
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(to_red(img))
    ax[1].imshow(to_green(img))
    ax[2].imshow(to_blue(img))

    plt.show()

if __name__ == "__main__":
    main()
