import math

def f(x):
    return x - math.floor((x % 6 )/3) - 4*math.floor((x % 6)/5) - 2*math.floor(x / 6)


for i in range(12):
    print(f(i))
