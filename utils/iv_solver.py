import math

def d_1_d2(s:float, k:float, r:float, sigma:float, t:float):
    d1 = (math.log(s/k) + (r + sigma**2 / 2)*t)/sigma/math.sqrt(t)
    d2 = d1 - sigma * math.sqrt(t)

    return d1, d2