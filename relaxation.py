import numpy as np

def solver(V, mask, tolerance, maxIterCount):
    nx, ny = V.shape
    for iter in range(maxIterCount):
        Vnew = V.copy()
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                if not mask[i,j]:
                    Vnew[i,j] = jacobiUpdate(V, i, j)
        diff = np.max(np.abs(Vnew[~mask] - V[~mask]))
        V = Vnew
        if diff < tolerance:
            return V, iter+1, diff
    raise RuntimeError("Solver reached maximum iteration count")
def jacobiUpdate(V, i, j):
   return 1/4 * (V[i+1, j] + V[i-1, j] + V[i, j+1] + V[i, j-1])