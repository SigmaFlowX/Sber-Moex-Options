import math

def d_1_d2(s:float, k:float, r:float, sigma:float, t:float):
    d1 = (math.log(s/k) + (r + sigma * sigma / 2)*t)/sigma/math.sqrt(t)
    d2 = d1 - sigma * math.sqrt(t)

    return d1,d2

def standard_normal_cdf(x:float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def standard_normal_pdf(x:float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)

def call_price(s:float, k:float, r:float, sigma:float, t:float):
    d1, d2 = d_1_d2(s, k, r, sigma, t)
    return s * standard_normal_cdf(d1) - k * math.exp(-r*t) * standard_normal_cdf(d2)

def put_price(s:float, k:float, r:float, sigma:float, t:float):
    d1, d2 = d_1_d2(s, k, r, sigma, t)
    return k * math.exp(-r*t) * standard_normal_cdf(-d2) - s * standard_normal_cdf(-d1)

def delta(s:float, k:float, r:float, sigma:float, t:float, type:str):
    d1, d2 = d_1_d2(s, k, r, sigma, t)
    y = standard_normal_cdf(d1)
    if type == "CALL":
        return y
    elif type == "PUT":
        return y-1
    else:
        raise Exception("invalid option type")

def gamma(s:float, k:float, r:float, sigma:float, t:float):
    d1, d2 = d_1_d2(s, k, r, sigma, t)
    return standard_normal_pdf(d1)/(s * sigma * math.sqrt(t))

def vega(s:float, k:float, r:float, sigma:float, t:float):
    d1, d2 = d_1_d2(s, k, r, sigma, t)
    return s * standard_normal_pdf(d1) * math.sqrt(t)
