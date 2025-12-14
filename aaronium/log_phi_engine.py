import sympy as sp

from .logs_phi import PHI, log_phi, ln
from .taylor_engine import taylor_series, taylor_iterate


def taylor_log_phi(about=1, order=6):
    """
    Taylor polynomial for log_phi(x) about x=about.
    Returns a SymPy expression in symbol x.
    """
    x = sp.Symbol("x")
    expr = sp.log(x, PHI)  # same as log_phi(x), but symbolic in x
    return taylor_series(expr, x, about=sp.sympify(about), order=order)


import sympy as sp
import mpmath as mp

PHI = (1 + sp.sqrt(5)) / 2  # keep your symbolic PHI too

def solve_log_phi(y, x0=2, steps=25, tol=1e-12, return_history=False, dps=50):
    """
    Solve log_phi(x) = y for x, numerically (Newton), using mpmath.
    log_phi(x) = ln(x)/ln(phi).
    """
    mp.mp.dps = dps
    phi = (1 + mp.sqrt(5)) / 2
    lnphi = mp.log(phi)

    y = mp.mpf(y)
    x = mp.mpf(x0)

    history = []
    for i in range(steps):
        # f(x) = ln(x)/ln(phi) - y
        fx = mp.log(x) / lnphi - y
        # f'(x) = 1/(x*ln(phi))
        dfx = 1 / (x * lnphi)

        x_new = x - fx / dfx

        if return_history:
            history.append((i, x, fx, x_new))

        if mp.fabs(x_new - x) < tol:
            x = x_new
            break

        x = x_new

    return (x, history) if return_history else x


def check_identity(k=3):
    """
    Safe identity check: log_phi(PHI**k) == k
    """
    k = sp.sympify(k)
    expr = sp.log(PHI**k) / sp.log(PHI)
    return sp.simplify(expr.rewrite(sp.log))


if __name__ == "__main__":
    print("Running log_phi_engine directly\n")

    # 1) Show a Taylor polynomial for log_phi(x) about x=1
    poly = taylor_log_phi(about=1, order=6)
    print("Taylor(log_phi(x)) about x=1, order=6:")
    print(poly)
    print()

    # 2) Identity check: log_phi(PHI**k) = k
    print("Identity check log_phi(PHI**3) =")
    print(check_identity(3))
    print()

    # 3) Inverse solve: given y, recover x ~ PHI**y
    y = 3
    x_hat = solve_log_phi(y, x0=2)
    print("x_hat =", x_hat)
    print("PHI**y =", mp.power((1+mp.sqrt(5))/2, y))
    print("difference =", x_hat - mp.power((1+mp.sqrt(5))/2, y))


if __name__ == "__main__":
    print("Running log_phi_engine with iteration history\n")

    y = 3
    result, history = solve_log_phi(
        y,
        x0=2,
        steps=15,
        tol=1e-12,
        return_history=True
    )

    print(f"Solving log_phi(x) = {y}")
    print()

    for i, val in enumerate(history):
        print(f"Iteration {i}: x = {val}")

    print()
    print("Final approximation:", result)
    print("Exact PHI**y:", sp.N(PHI**y))
    print("Error:", sp.N(result - PHI**y))

