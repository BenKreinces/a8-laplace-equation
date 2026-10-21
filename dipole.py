import numpy as np
import matplotlib.pyplot as plt
import relaxation
from pathlib import Path
Path("data").mkdir(exist_ok=True)
N=100
L=1
h = L/N
x = np.linspace(h/2, L-h/2, N)
y = np.linspace(h/2, L-h/2, N)
X , Y = np.meshgrid(x,y,indexing="ij")

mask4 = np.zeros((N,N), dtype=bool)
mask4[0,:] = True
mask4[-1,:] = True
mask4[:,0] = True
mask4[:,-1] = True


r1 = np.sqrt((X-L/3)**2 + (Y-L/2)**2)
r2 = np.sqrt((X-2*L/3)**2 + (Y-L/2)**2)
a = 0.05*L
shellCells1 = r1 <= a
shellCells2 = r2 <= a
mask4[shellCells1] = True
mask4[shellCells2] = True


V4 = np.zeros((N,N))
V4[shellCells1] = 1
V4[shellCells2] = -1
Vfinal, iterations, diff = relaxation.solver(V4, mask4, 1e-6, 100000)

np.savetxt("data/dipole.csv", np.column_stack((X.ravel(), Y.ravel(), Vfinal.ravel())),
           delimiter=",", header="x,y,V")
print(f"dipole: iterations = {iterations}, final difference = {diff}")
