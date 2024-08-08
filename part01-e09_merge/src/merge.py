#!/usr/bin/env python3

def bubbleSort(L):
    L = L.copy()
    n = len(L)
    for i in range(n-1):
        for j in range(n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L

def merge(L1, L2):
    L = L1 + L2
    return bubbleSort(L)

def main():
    pass

if __name__ == "__main__":
    main()
