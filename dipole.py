import numpy as np
import matplotlib.pyplot as plt
from plot_results import plot

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
plot(V4, mask4, "dipole")
