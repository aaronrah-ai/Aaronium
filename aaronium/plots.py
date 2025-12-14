import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"
IMAGE_DIR.mkdir(exist_ok=True)

import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

# constants
phi = (1 + mp.sqrt(5)) / 2
lnphi = mp.log(phi)

def log_phi(x):
    return mp.log(x) / lnphi


def plot_log_phi(x_min=0.5, x_max=5, n=400):
    xs = np.linspace(x_min, x_max, n)
    ys = [log_phi(x) for x in xs]

    plt.figure()
    plt.plot(xs, ys)
    plt.xlabel("x")
    plt.ylabel("log_phi(x)")
    plt.title("log_phi(x)")
    plt.grid(True)
    plt.savefig(IMAGE_DIR / "log_phi.png", dpi=200, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    plot_log_phi()

def plot_taylor_vs_exact(order=5, center=1):
    import sympy as sp

    x = sp.Symbol("x")
    expr = sp.log(x) / sp.log((1 + sp.sqrt(5)) / 2)
    taylor = sp.series(expr, x, center, order).removeO()

    f_exact = sp.lambdify(x, expr, "numpy")
    f_taylor = sp.lambdify(x, taylor, "numpy")

    xs = np.linspace(0.5, 2, 400)

    plt.figure()
    plt.plot(xs, f_exact(xs), label="Exact")
    plt.plot(xs, f_taylor(xs), linestyle="--", label=f"Taylor (order {order})")
    plt.legend()
    plt.grid(True)
    plt.title("log_phi(x): exact vs Taylor")
    plt.savefig(IMAGE_DIR / "taylor_vs_exact.png", dpi=200, bbox_inches="tight")
    plt.close()

def plot_log_phi_convergence(y=3, x0=2, steps=10):
    import mpmath as mp

    mp.mp.dps = 50
    phi = (1 + mp.sqrt(5)) / 2
    lnphi = mp.log(phi)

    x = mp.mpf(x0)
    xs = []

    for _ in range(steps):
        fx = mp.log(x) / lnphi - y
        dfx = 1 / (x * lnphi)
        x = x - fx / dfx
        xs.append(float(x))

    plt.figure()
    plt.plot(range(len(xs)), xs, marker="o")
    plt.xlabel("Iteration")
    plt.ylabel("x estimate")
    plt.title("Convergence of log_phi solver")
    plt.grid(True)

    plt.savefig(IMAGE_DIR /"log_phi_convergence.png", dpi=200, bbox_inches="tight")
    plt.close()

def plot_taylor_orders(orders=(2, 4, 6), center=1):
    import sympy as sp

    x = sp.Symbol("x")
    expr = sp.log(x) / sp.log((1 + sp.sqrt(5)) / 2)

    xs = np.linspace(0.5, 2, 400)
    f_exact = sp.lambdify(x, expr, "numpy")

    plt.figure()
    plt.plot(xs, f_exact(xs), label="Exact", linewidth=2)

    for o in orders:
        t = sp.series(expr, x, center, o).removeO()
        f_t = sp.lambdify(x, t, "numpy")
        plt.plot(xs, f_t(xs), linestyle="--", label=f"Order {o}")

    plt.legend()
    plt.grid(True)
    plt.title("Taylor Approximations of log_phi(x)")

    plt.savefig(IMAGE_DIR/"taylor_orders.png", dpi=200, bbox_inches="tight")
    plt.close()

def plot_digit_integration(n=23, base=4):
    digits = []
    value = n
    while value > 0:
        digits.append(value % base)
        value //= base
    digits = digits[::-1]

    integral = np.cumsum(digits)

    plt.figure()
    plt.step(range(len(digits)), digits, label="Digits", where="mid")
    plt.plot(range(len(integral)), integral, marker="o", label="Integrated digits")
    plt.legend()
    plt.grid(True)
    plt.title("Discrete Integration of NumberObject Digits")

    plt.savefig("images/digit_integration.png", dpi=200, bbox_inches="tight")
    plt.close()

    print("saving images to:", IMAGE_DIR)