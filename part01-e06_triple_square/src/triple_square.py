#!/usr/bin/env python3

def triple(x):
    return 3 * x

def square(x):
    return x ** 2

def main():
    for i in range(1, 11):
        a = square(i)
        b = triple(i)
        if a > b:
            break
        else:
            print(f"triple({i})=={b} square({i})=={a}")

if __name__ == "__main__":
    main()