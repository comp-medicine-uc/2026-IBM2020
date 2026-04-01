import numpy as np

def damped_oscillation(x, k, omega):
    return np.exp(-x)*np.cos(omega*x)