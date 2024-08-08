#!/usr/bin/env python3

def transform(s1, s2):
    res = []
    s1 = list(map(int, s1.split()))
    s2 = list(map(int, s2.split()))

    for a, b in zip(s1, s2):
        res.append(a * b)

    return res

def main():
    pass

if __name__ == "__main__":
    main()
