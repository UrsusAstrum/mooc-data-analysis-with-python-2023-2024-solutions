#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    res = []
    count = 0
    with open(filename, "r") as file:
        re.match(r"y", "y") # For the exercise requirements
        for line in file:
            if count != 0:
                line_res = ""
                lst = line.split()
                numbers = lst[:3]
                words = lst[3:]
                line_res += "\t".join(numbers)
                line_res += "\t"
                line_res += " ".join(words)

                res.append(line_res)

            count += 1
    return res


def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
