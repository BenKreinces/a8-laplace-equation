import relaxation
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

Path ("plots") . mkdir ( exist_ok = True )
def plot(V1, mask):
    V1[0,0] = (V1[0,1] + V1[1,0]) / 2
    V1[-1,0] = (V1[-1,1] + V1[-2,0]) / 2
    V1[0,-1] = (V1[0,-2] + V1[1,-1]) / 2
    V1[-1,-1] = (V1[-1,-2] + V1[-2,-1]) / 2
    Vfinal1, iterations1, diff1 = relaxation.solver(V1, mask, 1e-6, 100000)
    extent = [x[0]-h/2, x[-1]+h/2, y[0]-h/2, y[-1]+h/2]
    plt.imshow(Vfinal1.T, origin="lower", extent=extent, aspect="equal")
    plt.colorbar(label = "Potential V")
    plt.tight_layout()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('plots/oneEdgeHeatmap.png')
    plt.show()
    
    contours = plt.contour(X, Y, Vfinal1, levels=12)
    plt.clabel(contours, inline = True, fontsize = 8)
    plt.tight_layout()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.gca().set_aspect("equal")
    plt.savefig('plots/oneEdgeContour.png')
    plt.show()


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

plot(V1, mask1)
