import numpy as np
from pathlib import Path
import relaxation
Path("data").mkdir(exist_ok=True)

N=100
L=1
h = L/N
x = np.linspace(h/2, L-h/2, N)
y = np.linspace(h/2, L-h/2, N)
X , Y = np.meshgrid(x,y,indexing="ij")


mask3 = np.zeros((N,N), dtype=bool)
mask3[0,:] = True
mask3[-1,:] = True
mask3[:,0] = True
mask3[:,-1] = True


r = np.sqrt((X-L/2)**2 + (Y-L/2)**2)
R = L/3
t = 0.05*L
shellCells = (r>= R-t/2) & (r<= R+t/2)
mask3[shellCells] = True


V3 = np.zeros((N,N))
V3[:,-1] = 5
V3[0,:] = 5
V3[:,0] = 5
V3[-1,:] = 5
V3[shellCells & (Y>=L/2)] = 10
V3[shellCells & (Y<L/2)] = -10

Vfinal, iterations, diff = relaxation.solver(V3, mask3, 1e-6, 100000)

np.savetxt("data/splitShell.csv", np.column_stack((X.ravel(), Y.ravel(), Vfinal.ravel())), delimiter=",", header="x,y,V")
print("splitShell:", "iterations =", iterations, "final difference =", diff)