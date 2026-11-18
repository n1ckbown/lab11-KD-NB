"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

<<<<<<< HEAD
def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

=======
>>>>>>> c81b1d990e6b301b5c4a5075ab52b9662a9bb90a
def add(a, b):
    return a + b

def subtract(a, b):
    return a-b

def logarithm(a, b):
    if a < 0 or b < 0:
        raise ValueError
    else:
        return math.log(a,b)

def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def exp(a,b):
    return a ** b




