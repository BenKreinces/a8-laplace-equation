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
#Geometry A
mask1 = np.zeros((N,N), dtype=bool)
mask1[0,:] = True
mask1[-1,:] = True
mask1[:,0] = True
mask1[:,-1] = True
V1 = np.zeros((N,N))
V1[:,-1] = 1

plot(V1, mask1)

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

plot(V2, mask2)