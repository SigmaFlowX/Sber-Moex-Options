import math

def d_1_d2(s:float, k:float, r:float, sigma:float, t:float):
    d1 = (math.log(s/k) + (r + sigma * sigma / 2)*t)/sigma/math.sqrt(t)
    d2 = d1 - sigma * math.sqrt(t)

    return d1,d2

def standard_normal_cdf(x:float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def standard_normal_pdf(x:float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)

def price(s:float, k:float, r:float, sigma:float, t:float, option_type:str):
    d1, d2 = d_1_d2(s, k, r, sigma, t)
    if option_type == "CALL":
        return s * standard_normal_cdf(d1) - k * math.exp(-r*t) * standard_normal_cdf(d2)
    elif option_type == "PUT":
        return k * math.exp(-r * t) * standard_normal_cdf(-d2) - s * standard_normal_cdf(-d1)
    else:
        raise Exception("invalid option type")

def delta(s:float, k:float, r:float, sigma:float, t:float, option_type:str):
    d1, d2 = d_1_d2(s, k, r, sigma, t)
    y = standard_normal_cdf(d1)
    if option_type == "CALL":
        return y
    elif option_type == "PUT":
        return y-1
    else:
        raise Exception("invalid option type")

def gamma(s:float, k:float, r:float, sigma:float, t:float):
    d1, d2 = d_1_d2(s, k, r, sigma, t)
    return standard_normal_pdf(d1)/(s * sigma * math.sqrt(t))

def vega(s:float, k:float, r:float, sigma:float, t:float):
    d1, d2 = d_1_d2(s, k, r, sigma, t)
    return s * standard_normal_pdf(d1) * math.sqrt(t)

def theta(s:float, k:float, r:float, sigma:float, t:float, option_type:str):
    d1, d2 = d_1_d2(s, k, r, sigma, t)

    if option_type == "CALL":
        return -(s*standard_normal_pdf(d1) * sigma)/(2*math.sqrt(t)) - r*k*math.exp(-r*t)*standard_normal_cdf(d2)
    elif option_type == "PUT":
        return -(s*standard_normal_pdf(d1) * sigma)/(2*math.sqrt(t)) + r*k*math.exp(-r*t)*standard_normal_cdf(-d2)
    else:
        raise Exception("invalid option type")

def greek_black_scholes(theta:float, gamma:float, delta: float, sigma:float, r:float, s:float, v:float):
    return theta + sigma*sigma*s*s*gamma / 2 + r * s * delta - r * v
