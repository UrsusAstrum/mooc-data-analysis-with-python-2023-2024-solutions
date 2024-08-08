#!/usr/bin/env python3

import re

def integers_in_brackets(s):
    res = []
    s = ''.join(s.split())
    tup = re.findall(r"\[[+-]?\d+\]", s)
    for i in range(len(tup)):
        res.append(tup[i])
        res[i] = res[i].replace("[", "")
        res[i] = res[i].replace("]", "")
        res[i] = res[i].replace("+", "")
        res[i] = int(res[i])
    return res

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
