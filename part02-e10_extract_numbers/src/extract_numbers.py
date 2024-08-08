#!/usr/bin/env python3

def extract_numbers(s):
    s_list = s.split()
    res = []
    for val in s_list:
        try:
            res.append(int(val))
        except ValueError:
            try:
                res.append(float(val))
            except ValueError:
                continue
    return res

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
