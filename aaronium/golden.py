import sympy as sp
from .logs_phi import PHI, log_phi, ln, log10


def golden_ratio():
    """Return the golden ratio constant PHI"""
    return PHI


def golden_sample(lambda_value=0):
    """
    Page-125 style expression:
    (4/3) * pi * ln(41.5) * (pi * ln(58.5)) + lambda
    """
    lam = sp.sympify(lambda_value)
    pi = sp.pi
    result = (sp.Rational(4, 3) * pi * ln(41.5)) * (pi * ln(58.5)) + lam
    return sp.simplify(result)


def golden_mistake(lambda_value=0):
    """
    Intentional 'golden mistake' variant.
    Currently mirrors golden_sample.
    """
    return golden_sample(lambda_value=lambda_value)


__all__ = ["golden_ratio", "golden_sample", "golden_mistake"]


if __name__ == "__main__":
    print("running golden.py directly\n")

    print("PHI =", PHI)
    print("golden_ratio() =", golden_ratio())
    print("ln(5) =", ln(5))
    print("log10(41.5) =", log10(41.5))
    print("log_phi(41.5) =", log_phi(41.5))
    print("golden_sample() =", golden_sample())