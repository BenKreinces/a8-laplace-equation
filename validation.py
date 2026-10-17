import numpy as np
import relaxation
N = 100
L=1
h = L/N
x = np.linspace(h/2, L-h/2, N)
y = np.linspace(h/2, L-h/2, N)
X , Y = np.meshgrid(x,y,indexing="ij")
mask = np.zeros((N, N), dtype = bool)
mask[0,:] = True
mask[-1,:] = True
mask[:,0] = True
mask[:,-1] = True
V = np.zeros((N,N))
V[mask] = 1
Vfinal, iterations, diff = relaxation.solver(V, mask, 1e-6, 100000)
error = np.max(np.abs(Vfinal[~mask]-1))
print(error)