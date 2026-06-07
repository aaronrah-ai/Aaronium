import numpy as np
from core.engine import AaroniumEngine

def func(x):
    return np.sin(x) + 0.1 * x**2

x_values = np.linspace(-5, 5, 50)

engine = AaroniumEngine(order=4)

result = engine.run(func, x_values)

print("Best Transform:", result["transform"])
print("Error:", result["error"])
