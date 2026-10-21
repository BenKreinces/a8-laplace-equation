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
#Geometry A
mask1 = np.zeros((N,N), dtype=bool)
mask1[0,:] = True
mask1[-1,:] = True
mask1[:,0] = True
mask1[:,-1] = True
V1 = np.zeros((N,N))
V1[:,-1] = 1

Vfinal, iterations, diff = relaxation.solver(V1, mask1, 1e-6, 100000)
np.savetxt("data/oneEdge.csv", np.column_stack((X.ravel(), Y.ravel(), Vfinal.ravel())),delimiter=",", header="x,y,V")
print(f"oneEdge: iterations = {iterations}, final difference = {diff}")
