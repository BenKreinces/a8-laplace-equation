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


V2 = np.zeros((N,N))
vals = X/L
V2[mask] = vals[mask]
Vfinal2, iterations2, diff2 = relaxation.solver(V2, mask, 1e-6, 100000)
error2 = np.max(np.abs(Vfinal2[~mask]-vals[~mask]))
print(error2)


