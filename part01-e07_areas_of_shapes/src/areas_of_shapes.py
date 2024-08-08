#!/usr/bin/env python3

import math

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "triangle":
            base = input("Give base of the triangle: ")
            height = input("Give height of the triangle: ")
            print(f"The area is {0.5 * float(base) * float(height):.6f}")

        elif shape == "rectangle":
            width = input("Give width of the rectangle: ")
            height = input("Give height of the rectangle: ")
            print(f"The area is {float(width) * float(height):.6f}")

        elif shape == "circle":
            radius = input("Give radius of the circle: ")
            print(f"The area is {math.pi * float(radius) ** 2 :.6f}")
        
        elif shape == "":
            break

        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()