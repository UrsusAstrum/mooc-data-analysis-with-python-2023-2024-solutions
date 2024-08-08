#!/usr/bin/env python3

def sum_equation(L):
    total = sum(L)
    L = [str(i) for i in L]
    if len(L) == 0:
        return "0 = 0"
    res = " + ".join(L)
    res += f" = {total}"
    return res

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
