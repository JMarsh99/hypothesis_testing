import math


def run_complicated_maths_function_1(a: float, b: float, c: float, d: float):
    return (pow(a, b) / math.sqrt(c - d)) / pow(d * 4, 4) - abs(a)


def run_complicated_maths_function_2(a: float, b: float, c: float, d: float):
    return ((298 * a) ^ (1 / math.sin(d))) ^ (0.5 * c) - c * b


def run_complicated_maths_function_3(a: float, b: float, c: float, d: float):
    return math.pi * math.log(a, b) * math.log(c, d)


def run_complicated_maths_function_4(a: float, b: float, c: float, d: float):
    return max(abs(a) - abs(b), pow(b, 89)) - (d / math.radians(123 + c))
