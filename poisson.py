import relaxation
import numpy as np
import matplotlib.pyplot as plt

def plot(V1, mask, source, h):
    V1[0,0] = (V1[0,1] + V1[1,0]) / 2
    V1[-1,0] = (V1[-1,1] + V1[-2,0]) / 2
    V1[0,-1] = (V1[0,-2] + V1[1,-1]) / 2
    V1[-1,-1] = (V1[-1,-2] + V1[-2,-1]) / 2
    Vfinal1, iterations1, diff1 = relaxation.solver(V1, mask, 1e-6, 100000, source=source, h=h)
    plt.imshow(Vfinal1.T, origin="lower", aspect="equal")
    plt.colorbar(label = "Potential V")
    plt.tight_layout()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('poissonHeatmap.png')
    plt.show()
    contours = plt.contour(X, Y, Vfinal1, levels=12)
    plt.clabel(contours, inline = True, fontsize = 8)
    plt.tight_layout()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.gca().set_aspect("equal")
    plt.savefig('PoissonContour.png')
    plt.show()

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


plot(V3, mask3, source, h)

