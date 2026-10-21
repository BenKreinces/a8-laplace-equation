import numpy as np
import matplotlib.pyplot as plt
from plot_results import plot
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

plot(V1, mask1, "oneEdge")
