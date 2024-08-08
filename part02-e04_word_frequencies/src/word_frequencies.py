#!/usr/bin/env python3

def word_frequencies(filename):
    res = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.split()
            print(line)
            for word in line:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word not in res.keys():
                    res[word] = 1
                else:
                    res[word] += 1

    return res

def main():
    word_frequencies("alice.txt")

if __name__ == "__main__":
    main()
