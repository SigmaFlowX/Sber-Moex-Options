import math

def d_1_d2(s:float, k:float, r:float, sigma:float, t:float) -> float:
    d1 = (math.log(s/k) + (r + sigma * sigma / 2)*t)/sigma/math.sqrt(t)
    d2 = d1 - sigma * math.sqrt(t)

    return d1, d2

def standard_normal_cdf(x:float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def standard_normal_pdf(x:float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)
