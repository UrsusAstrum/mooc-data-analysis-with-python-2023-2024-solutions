#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    res = []
    with open(filename, "r") as file:
        for line in file:
            numbers = re.findall(r"\b[0-9]+\b", line)
            numbers = [int(i) for i in numbers]
            month = re.findall(r"Oct | Nov | Dec", line)
            line = line.split()
            
            res.append((numbers[1], month[0].strip(), *numbers[2:5], line[-1]))

    return res

def main():
    pass

if __name__ == "__main__":
    main()
