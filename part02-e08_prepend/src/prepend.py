#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, start):
        self.start = start

    def write(self, s):
        print(f"{self.start}{s}")

def main():
    pass

if __name__ == "__main__":
    main()
