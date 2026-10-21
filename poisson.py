import numpy as np
import matplotlib.pyplot as plt
from plot_results import plot

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
plot(V3, mask3, "poisson", source, h)

