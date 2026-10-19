import relaxation
import numpy as np
import matplotlib.pyplot as plt

def plot(V1, mask):
    V1[0,0] = (V1[0,1] + V1[1,0]) / 2
    V1[-1,0] = (V1[-1,1] + V1[-2,0]) / 2
    V1[0,-1] = (V1[0,-2] + V1[1,-1]) / 2
    V1[-1,-1] = (V1[-1,-2] + V1[-2,-1]) / 2
    Vfinal1, iterations1, diff1 = relaxation.solver(V1, mask, 1e-6, 100000)
    plt.imshow(Vfinal1.T, origin="lower", aspect="equal")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    plt.contour(X, Y, Vfinal1, levels=12)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.gca().set_aspect("equal")
    plt.show()

N=100
L=1
h = L/N
x = np.linspace(h/2, L-h/2, N)
y = np.linspace(h/2, L-h/2, N)
X , Y = np.meshgrid(x,y,indexing="ij")

#Geometry D
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
V4[:,-1] = 5
V4[0,:] = 5
V4[:,0] = 5
V4[-1,:] = 5
V4[shellCells1] = 1
V4[shellCells2] = -1
plot(V4, mask4)
