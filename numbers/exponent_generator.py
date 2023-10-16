gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
    
def get_exponent(phi):
    for e in range(3, phi - 1):
        if gcd(e, phi) == 1:
            return e    
