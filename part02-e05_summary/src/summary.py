#!/usr/bin/env python3

import sys
import math
import statistics

def summary(filename):
    res = []
    with open(filename, "r") as file:
        nums = []
        for line in file:
            try:
                x = float(line)
            except ValueError:
                continue
            nums.append(x)

    return (sum(nums), sum(nums) / len(nums), statistics.stdev(nums))

def main():
    for i in sys.argv[1:]:
        res = summary(i)
        print(f"File: {i} Sum: {res[0]:6f} Average: {res[1]:6f} Stddev: {res[2]:6f}")

if __name__ == "__main__":
    main()
