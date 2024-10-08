#!/usr/bin/env python3

def reverse_dictionary(d):
    res = {}

    for key, value in d.items():
        for i in value:
            if i in res:
                res[i].append(key)
            else:
                res[i] = [key]
    return res

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
