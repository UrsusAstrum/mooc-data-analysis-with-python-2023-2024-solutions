#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename, "r") as file:
        lines, words, chars = (0, 0, 0)
        for line in file:
            lines += 1
            word_list = line.split()
            words += len(word_list)
            for word in line:
                chars += len(word)
    return (lines, words, chars)

def main():
    for i in sys.argv[1:]:
        res = file_count(i)
        print(f"{res[0]}\t{res[1]}\t{res[2]}\t{i}")

if __name__ == "__main__":
    main()
