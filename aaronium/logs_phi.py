import sympy as sp

# Golden ratio constant
PHI = (1 + sp.sqrt(5)) / 2


def log_phi(x):
    """Logarithm base PHI"""
    x = sp.sympify(x)
    return sp.log(x, PHI)


def ln(x):
    """Natural logarithm"""
    x = sp.sympify(x)
    return sp.log(x)


def log10(x):
    """Base-10 logarithm"""
    x = sp.sympify(x)
    return sp.log(x, 10)


def log_base(x, base):
    """Logarithm with arbitrary base"""
    x = sp.sympify(x)
    base = sp.sympify(base)
    return sp.log(x) / sp.log(base)


if __name__ == "__main__":
    print("PHI =", PHI)
    print("ln(5) =", ln(5))
    print("log10(41.5) =", log10(41.5))
    print("log_phi(41.5) =", log_phi(41.5))