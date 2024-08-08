#!/usr/bin/env python3

class Rational(object):
    def __init__(self, num, dem):
        self.num = num
        self.dem = dem
        self.val = num / dem

    def __add__(self, addend):
        if isinstance(addend, Rational):
            return (self.num * addend.dem + self.dem * addend.num) / (self.dem * addend.dem)
        else:
            return self.val + addend
    
    def __sub__(self, subtrahend):
        if isinstance(subtrahend, Rational):
            return (self.num * subtrahend.dem - self.dem * subtrahend.num) / (self.dem * subtrahend.dem)
        else:
            return self.val - subtrahend
    
    def __mul__(self, factor):
        if isinstance(factor, Rational):
            return self.val * factor.val
        else:
            return self.val * factor
    
    def __truediv__(self, divisor):
        if isinstance(divisor, Rational):
            return self.val / divisor.val
        else:
            return self.val / divisor
    
    def __eq__(self, expression):
        if isinstance(expression, Rational):
            return self.val == expression.val
        else:
            return self.val == expression
    
    def __gt__(self, expression):
        if isinstance(expression, Rational):
            return self.val > expression.val
        else:
            return self.val > expression

    def __lt__(self, expression):
        if isinstance(expression, Rational):
            return self.val < expression.val
        else:
            return self.val < expression
    
    def __repr__(self):
        return f"{self.num} / {self.dem}"

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
