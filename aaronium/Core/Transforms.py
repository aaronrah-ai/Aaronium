import numpy as np

phi = (1 + 5 ** 0.5) / 2

def identity(x):
    return x

def log_transform(x):
    return np.log(np.abs(x) + 1e-8)

def phi_scale(x):
    return x * phi

def normalize(x):
    return (x - np.mean(x)) / (np.std(x) + 1e-8)

TRANSFORMS = {
    "identity": identity,
    "log": log_transform,
    "phi_scale": phi_scale,
    "normalize": normalize
}
