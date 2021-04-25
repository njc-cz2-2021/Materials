def cube(x):
    return x**3

def div_algo(a,b):
    if a>b:
        a,b=b,a
    return f'{b}={b//a}*{a}+{b%a}'

def gcd_euclid(a,b):
    if a>b:
        a,b=b,a
    if b%a==0:
        return a
    else:
        return gcd_euclid(a,b-(b//a)*a)

def lcm(a,b):
    return (a*b)/gcd_euclid(a,b)