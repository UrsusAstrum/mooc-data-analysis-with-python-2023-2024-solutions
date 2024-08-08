#!/usr/bin/env python3

def distinct_characters(L):
    res = {}
    for i in L:
        res[i] = len(set(i))

    return res

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
