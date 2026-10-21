import numpy as np
import matplotlib.pyplot as plt
from plot_results import plot
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

plot(V2, mask2, "fourEdge")
