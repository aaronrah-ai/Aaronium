"""Basic arithmetic ideas: repeated addition as multiplication, etc."""
import sympy as sp

def repeated_addition(base, times):
    """Return base added to itself 'times' times."""
    base = sp.sympify(base)
    times = int(times)
    return sum(base for _ in range(times))

def square(n):
    n = sp.sympify(n)
    return n**2

def cube(n):
    n = sp.sympify(n)
    return n**3

__all__ = ['repeated_addition', 'square', 'cube']

if __name__== "__main__":
	print("running arithmetic.py directly")

	print("repeated addition(3, 4) =", repeated_addition(3, 4))
	print("square(5) =", square(5))
	print("cube(2) =", cube(2))