def simplify_fraction(fraction):
    nominator, denumenator = fraction
    gcd = find_gcd(nominator, denumenator)
    return (nominator / gcd, denumenator / gcd)


def find_gcd(a, b):
    return a if a - b == 0 else find_gcd(abs(a - b), min(a, b))
