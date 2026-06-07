from core.taylor import taylor_approx
from core.metrics import mse

def select_best_transform(func, x_values, transforms, order=5):
    best_score = float("inf")
    best_result = None

    y_true = [func(x) for x in x_values]

    for name, transform in transforms.items():

        transformed_func = lambda x: transform(func(x))

        y_pred = [taylor_approx(transformed_func, x, order=order)
                  for x in x_values]

        error = mse(y_true, y_pred)

        if error < best_score:
            best_score = error
            best_result = {
                "transform": name,
                "error": error,
                "prediction": y_pred
            }

    return best_result