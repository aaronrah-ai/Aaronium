import numpy as np

def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def taylor_approx(f, x, x0=0, order=5):
    approx = f(x0)

    for n in range(1, order + 1):
        deriv = f
        for _ in range(n):
            deriv = lambda t, d=deriv: numerical_derivative(d, t)

        approx += deriv(x0) * (x - x0) ** n / np.math.factorial(n)

    return approx
