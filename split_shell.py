import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from plot_results import plot

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

plot(V3, mask3, "splitShell")