"""
NumberObject System

Numbers are treated as structured objects with:
- value
- base representation
- digit structure
- discrete and continuous integration

This extends earlier base-conversion helpers into a true object system.
"""

import sympy as sp


class NumberObject:
    def __init__(self, value, base=10):
        self.value = int(value)
        self.base = int(base)
        self.digits = self.to_base(self.value, self.base)

    # ---------- Base mechanics ----------
    @staticmethod
    def to_base(n, base):
        n = int(n)
        base = int(base)
        if n == 0:
            return [0]
        digits = []
        while n > 0:
            digits.append(n % base)
            n //= base
        return digits[::-1]

    @staticmethod
    def from_base(digits, base):
        value = 0
        for d in digits:
            value = value * base + int(d)
        return value

    # ---------- Representations ----------
    def as_base(self, base):
        return NumberObject(self.value, base)

    def __repr__(self):
        return (
            f"NumberObject(value={self.value}, "
            f"base={self.base}, digits={self.digits})"
        )

    # ---------- Integration ----------
    def integrate_digits(self):
        """
        Discrete integration:
        Accumulate digit structure (Riemann-style sum).
        """
        integral = []
        running = 0
        for d in self.digits:
            running += d
            integral.append(running)
        return integral

    def integrate_continuous(self, symbol=sp.Symbol("x")):
        """
        Continuous integration:
        Treat value as a constant function.
        """
        f = sp.Integer(self.value)
        return sp.integrate(f, symbol)


# ---------- Convenience constructors ----------
def binary(n):
    return NumberObject(n, base=2)


def ternary(n):
    return NumberObject(n, base=3)


def quaternary(n):
    return NumberObject(n, base=4)


def quinary(n):
    return NumberObject(n, base=5)


__all__ = [
    "NumberObject",
    "binary",
    "ternary",
    "quaternary",
    "quinary",
]


# ---------- Test block ----------
if __name__ == "__main__":
    n = NumberObject(23, base=4)
    print(n)

    print("As binary:", n.as_base(2))
    print("Digit integral:", n.integrate_digits())
    print("Symbolic integral:", n.integrate_continuous())
