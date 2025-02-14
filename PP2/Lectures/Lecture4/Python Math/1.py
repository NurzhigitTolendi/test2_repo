import math

print(math.floor(3.9))  # 3 (округление вниз)
print(math.ceil(3.1))   # 4 (округление вверх)

print(round(3.5))  # 4
print(round(3.4))  # 3

print(math.pow(2, 3))   # 8.0 (2^3)
print(2 ** 3)          # 8 (то же самое, но без math)

print(math.sqrt(16))  # 4.0

def nth_root(x, n):
    return x ** (1/n)

print(nth_root(27, 3))  # 3.0 (кубический корень)

print(math.log(10))  # 2.302585

print(math.log(100, 10))  # 2.0

print(math.log2(8))  # 3.0

print(math.sin(math.radians(30)))  # 0.5
print(math.cos(math.radians(60)))  # 0.5
print(math.tan(math.radians(45)))  # 1.0

print(math.pi)   # 3.141592653589793
print(math.e)    # 2.718281828459045

import random
print(random.randint(1, 10))  # случайное число от 1 до 10
print(random.uniform(1, 10))  # случайное число с плавающей запятой
