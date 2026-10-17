import numpy as np

def solver(V, mask, tolerance, maxIterCount):
    for iter in range(maxIterCount):
        Vnew = V.copy()
        Vnew[1:-1, 1:-1] = 1/4 * (V[2:, 1:-1] + V[:-2, 1:-1] + V[1:-1, 2:] + V[1:-1, :-2])
        Vnew[mask] = V[mask]
        diff = np.max(np.abs(Vnew[~mask] - V[~mask]))
        V = Vnew
        if diff < tolerance:
            return V, iter+1, diff
    raise RuntimeError("Solver reached maximum iteration count")
