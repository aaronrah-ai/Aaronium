import sympy as sp
from .logs_phi import PHI, log_phi, ln, log10
LAMBDA_BOOK = 8.2954


def golden_ratio():
    """Return the golden ratio constant PHI"""
    return PHI


def golden_sample(lambda_value=0):
    """
    Page-125 style expression:
    (4/3) * pi * log10(41.5) * (pi * log10(58.5 + lambda))
    """
    lam = sp.sympify(lambda_value)
    pi = sp.pi
    result = (sp.Rational(4, 3) * pi * log10(41.5)) * (pi * log10(58.5 + lam))
    return sp.simplify(result)


def lambda_from_geometry():
    """
    Derive lambda from geometric normalization (book path)
    """
    return 100 * (sp.Rational(1,2) + sp.sqrt(1.25)) /(sp.sqrt(sp.Rational(65,4)/2) * 4.5)

def lambda_half_geometry():
    return 100 * (sp.Rational(1,2) + sp.sqrt(1.25)) / (
        (sp.sqrt(sp.Rational(65,4)) / 2) * 4.5
    )

def lambda_full_geometry():
    return 100 * (sp.Rational(1,2) + sp.sqrt(1.25)) / (
        sp.sqrt(sp.Rational(65,4)) * 4.5
    )


def golden_sample_book():
    """
    Book-specific evaluation using lambda = 8.2954
    """
    return golden_sample(lambda_value=LAMBDA_BOOK)


def golden_mistake(lambda_value=0):
    """
    Intentional 'golden mistake' variant.
    Currently mirrors golden_sample.
    """
    return golden_sample(lambda_value=lambda_value)


__all__ = ["golden_ratio", "golden_sample", "golden_mistake", "golden_sample_book"]


if __name__ == "__main__":
    print("running golden.py directly\n")

    print("PHI =", PHI)
    print("golden_ratio() =", golden_ratio())

    print("\n--- Log checks ---")
    print("ln(5) =", ln(5))
    print("log10(41.5) =", log10(41.5))
    print("log_phi(41.5) =", log_phi(41.5))

    print("\n--- Golden sample (symbolic) ---")
    print("golden_sample() =", golden_sample())

    print("\n--- Book evaluation ---")
    print("lambda (book) =", LAMBDA_BOOK)
    print("golden_sample_book() =", golden_sample_book())
    print("numeric =", golden_sample_book().evalf())

    lam = lambda_from_geometry()
    print("lambda (geometry) =", lam.evalf(6))
    print("lambda (half geometry) =", lambda_half_geometry().evalf(6))
    print("lambda (full geometry) =", lambda_full_geometry().evalf(6))

