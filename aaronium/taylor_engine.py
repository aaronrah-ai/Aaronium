import sympy as sp


def taylor_series(expr, var, about=0, order=5):
    """
    Return the Taylor polynomial of expr in variable var
    expanded about `about` up to given order.
    """
    var = sp.Symbol(str(var))
    series = sp.series(expr, var, about, order)
    return series.removeO()


def maclaurin_exp(x, order=5):
    """Maclaurin series approximation for e^x"""
    x_sym = sp.Symbol('x')
    series = taylor_series(sp.exp(x_sym), x_sym, 0, order)
    return series.subs(x_sym, x)


def maclaurin_ln1px(x, order=5):
    """Maclaurin series approximation for ln(1 + x)"""
    x_sym = sp.Symbol('x')
    series = taylor_series(sp.log(1 + x_sym), x_sym, 0, order)
    return series.subs(x_sym, x)


__all__ = ["taylor_series", "maclaurin_exp", "maclaurin_ln1px", "taylor_iterate",]



def taylor_iterate(expr, var, x0, steps=10, tol=1e-6, return_history=False):
    """
    Numerically iterate using a Taylor / Newton update.

    If return_history=True, returns (final_value, history)
    where history = [x0, x1, x2, ...]
    """
    var = sp.Symbol(str(var))
    current = sp.sympify(x0)
    history = [sp.N(current)]

    for i in range(steps):
        f_val = expr.subs(var, current)
        f_prime = sp.diff(expr, var).subs(var, current)

        if f_prime == 0:
            break

        next_val = current - f_val / f_prime
        history.append(sp.N(next_val))

        if abs(next_val - current) < tol:
            current = next_val
            break

        current = next_val

    if return_history:
        return sp.N(current), history

    return sp.N(current)

if __name__ == "__main__":
    print("Running taylor_engine directly\n")

    x = sp.Symbol('x')

    print("Taylor series for e^x about 0 (order 5):")
    print(taylor_series(sp.exp(x), x, 0, 5))
    print()

    print("Maclaurin exp approximation at x = 1:")
    print(maclaurin_exp(1, order=6))
    print("Exact:", sp.exp(1))
    print()

    print("Maclaurin ln(1+x) approximation at x = 0.5:")
    print(maclaurin_ln1px(0.5, order=6))
    print("Exact:", sp.log(1.5))


if __name__ == "__main__":
    x = sp.Symbol('x')

    print("Running taylor_engine directly\n")

    print("Taylor series for e^x about 0 (order 5):")
    print(taylor_series(sp.exp(x), x, 0, 5))
    print()

    expr = sp.log(x) - 1
    approx = taylor_iterate(expr, x, x0=2, steps=5)

    print("Solving ln(x) = 1 using Taylor iteration:")
    print("Approximation:", approx)
    print("Exact:", sp.E)
