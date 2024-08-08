#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    triangle.area(3, 4)
    triangle.hypotenuse(3, 4)

if __name__ == "__main__":
    main()
