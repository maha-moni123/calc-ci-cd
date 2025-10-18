import math

def two_plus_two():
    return "2+2=4"

def add(a: float, b: float) -> float: return float(a) + float(b)
def sub(a: float, b: float) -> float: return float(a) - float(b)
def mul(a: float, b: float) -> float: return float(a) * float(b)
def div(a: float, b: float) -> float:
    b = float(b)
    if b == 0.0: raise ZeroDivisionError("division by zero")
    return float(a) / b

# --- V1.2 scientific ops ---
def sqrt(x: float) -> float:
    x = float(x)
    if x < 0:
        raise ValueError("sqrt domain error (x < 0)")
    return math.sqrt(x)

def power(a: float, b: float) -> float:
    return math.pow(float(a), float(b))

def sin(x: float) -> float: return math.sin(float(x))
def cos(x: float) -> float: return math.cos(float(x))
def tan(x: float) -> float: return math.tan(float(x))
