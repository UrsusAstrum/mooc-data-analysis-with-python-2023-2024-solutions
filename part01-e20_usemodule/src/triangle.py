# Enter you module contents here
"""Module containing functions to calculate the hypotenuse and area of a right-angled triange."""
import math
def hypotenuse(a, b):
    """Calculates hypotenuse."""
    return math.sqrt(a ** 2 + b ** 2)

def area(a, b):
    """Calculates area."""
    return 0.5 * a * b

__version__ = "1.0"
__author__ = "jakps"