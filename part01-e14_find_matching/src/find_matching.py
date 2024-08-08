#!/usr/bin/env python3

def find_matching(L, pattern):
    res = []
    for idx, string in enumerate(L):
        if pattern in string:
            res.append(idx)

    return res


def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
