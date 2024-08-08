#!/usr/bin/env python3

def interleave(*lists):
    res = []
    lst = list(zip(*lists))
    for i in lst:
        res.extend(i)

    return res

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
