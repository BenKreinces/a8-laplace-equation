import numpy as np
import relaxation
from pathlib import Path
Path("data").mkdir(exist_ok=True)
N=100
L=1
h = L/N
x = np.linspace(h/2, L-h/2, N)
y = np.linspace(h/2, L-h/2, N)
X , Y = np.meshgrid(x,y,indexing="ij")

#Geometry B
mask2 = np.zeros((N,N), dtype=bool)
mask2[0,:] = True
mask2[-1,:] = True
mask2[:,0] = True
mask2[:,-1] = True
V2 = np.zeros((N,N))
V2[:,-1] = 1
V2[0,:] = -0.5
V2[:,0] = 0
V2[-1,:] = 0.2
V2[0,0] = (V2[0,1] + V2[1,0])/2
V2[-1,0] = (V2[-1,1] + V2[-2,0])/2
V2[0,-1] = (V2[0,-2] + V2[1,-1])/2
V2[-1,-1] = (V2[-1,-2] + V2[-2,-1])/2
Vfinal, iterations, diff = relaxation.solver(V2, mask2, 1e-6, 100000)
np.savetxt("data/fourEdge.csv", np.column_stack((X.ravel(), Y.ravel(), Vfinal.ravel())), delimiter=",", header="x,y,V", comments="")
print(f"fourEdge: iterations = {iterations}, final difference = {diff}")