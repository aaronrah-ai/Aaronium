from core.transforms import TRANSFORMS
from core.taylor import taylor_approx
from core.metrics import mse
from core.selector import select_best_transform

class AaroniumEngine:
    def __init__(self, transforms=None, order=5):
        self.transforms = transforms or TRANSFORMS
        self.order = order

    def run(self, func, x_values):
        best = select_best_transform(
            func,
            x_values,
            self.transforms,
            self.order
        )

        return best
