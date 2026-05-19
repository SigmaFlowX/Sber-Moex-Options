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
    d1, _ = d_1_d2(s, k, r, sigma, t)
    return standard_normal_pdf(d1)/(s * sigma * math.sqrt(t))

def vega(s:float, k:float, r:float, sigma:float, t:float):
    d1, _ = d_1_d2(s, k, r, sigma, t)
    return s * standard_normal_pdf(d1) * math.sqrt(t)

def theta(s:float, k:float, r:float, sigma:float, t:float, option_type:str):
    d1, d2 = d_1_d2(s, k, r, sigma, t)

    if option_type == "CALL":
        return -(s*standard_normal_pdf(d1) * sigma)/(2*math.sqrt(t)) - r*k*math.exp(-r*t)*standard_normal_cdf(d2)
    elif option_type == "PUT":
        return -(s*standard_normal_pdf(d1) * sigma)/(2*math.sqrt(t)) + r*k*math.exp(-r*t)*standard_normal_cdf(-d2)
    else:
        raise Exception("invalid option type")

def greek_black_scholes(theta_val:float, gamma_val:float, delta_val: float, sigma:float, r:float, s:float, v:float):
    return theta_val + sigma*sigma*s*s*gamma_val / 2 + r * s * delta_val - r * v


def iv_newton(s:float, k:float, r:float, t:float, market_price: float, option_type:str, eps: float, max_iter: int, allow_fallback=True) -> float:
    sigma_n = market_price / (s * 0.4 * t ** 0.5)
    sigma_n = max(1e-6, min(sigma_n, 10.0))
    for _ in range(max_iter):
        vega_val = vega(s, k, r, sigma_n, t)
        if vega_val < 1e-10:
            if allow_fallback:
                break
            else:
                raise ValueError("Vega is close to zero, Newton method is unstable")

        price_val = price(s, k, r, sigma_n, t, option_type)

        sigma_np1 = sigma_n - (price_val - market_price)/vega_val

        if abs(sigma_n - sigma_np1) < eps:
            return sigma_np1
        sigma_n = sigma_np1

    #bisection method
    a, b = 1e-6, 10.0

    if (price(s, k, r, a, t, option_type) - market_price) * (price(s, k, r, b, t, option_type) - market_price) > 0:
        raise ValueError("Backup bisection method is not applicable")

    for _ in range(max_iter):
        mid = (a + b) / 2
        if price(s, k, r, mid, t, option_type) - market_price > 0:
            b = mid
        else:
            a = mid
        if (b - a) < eps:
            return mid

    raise ValueError("IV not found")


def main():
    import time

    s = 323.57
    k = 320.0
    r = 0.13
    t = 4.0/365.0
    option_type = "CALL"
    eps = 0.0001
    market_price = 4.77
    max_iter = 100

    start_time = time.perf_counter()

    iv = iv_newton(s, k, r, t,market_price, option_type,eps, max_iter)

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    print(iv)
    print(f"Execution time: {execution_time * 1000} ms")

if __name__ == "__main__":
    main()