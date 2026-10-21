import numpy as np
import relaxation
from pathlib import Path
Path ("data") . mkdir ( exist_ok = True )
N=100
L=1
h = L/N
sigma = 0.08 * L
s0 = 100
x = np.linspace(h/2, L-h/2, N)
y = np.linspace(h/2, L-h/2, N)
X , Y = np.meshgrid(x,y,indexing="ij")
source = s0 * np.exp(-((X-L/2)**2 + (Y-L/2)**2) / (2 * sigma**2))
mask3 = np.zeros((N,N), dtype=bool)
mask3[0,:] = True
mask3[-1,:] = True
mask3[:,0] = True
mask3[:,-1] = True
V3 = np.zeros((N,N))
V3[:,-1] = 0
V3[0,:] = 0
V3[:,0] = 0
V3[-1,:] = 0


Vfinal, iterations, diff = relaxation.solver(V3, mask3, 1e-6, 100000, source=source, h=h)
np.savetxt("data/poisson.csv", np.column_stack((X.ravel(), Y.ravel(), Vfinal.ravel())),delimiter=",", header="x,y,V")
print(f"possion: iterations = {iterations}, final difference = {diff}")
i, j = np.unravel_index(np.argmax(Vfinal), Vfinal.shape)
print(f"Maximum potential:{Vfinal[i,j]} at{(X[i,j], Y[i,j])}")
Vzero, _, _ = relaxation.solver(np.zeros_like(V3), mask3, 1e-6, 100000, h=h)
print(f"Zero-source maximum absolute potential: {np.max(np.abs(Vzero))}")


