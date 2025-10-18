import math

def two_plus_two():
    return "2+2=4"

def add(a: float, b: float) -> float:
    return float(a) + float(b)

def sub(a: float, b: float) -> float:
    return float(a) - float(b)

def mul(a: float, b: float) -> float:
    return float(a) * float(b)

def div(a: float, b: float) -> float:
    b = float(b)
    if b == 0.0:
        raise ZeroDivisionError("division by zero")
    return float(a) / b
