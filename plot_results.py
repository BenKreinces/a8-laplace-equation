import relaxation
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
Path ("plots") . mkdir ( exist_ok = True )

def plot(name):
    data = np.loadtxt(f"data/{name}.csv", delimiter=",", skiprows=1)
    x = np.unique(data[:, 0])
    y = np.unique(data[:, 1])
    V = data[:, 2].reshape((len(x), len(y)))
    X, Y = np.meshgrid(x, y, indexing="ij")
    h = x[1] - x[0]
    L = len(x) * h
    extent = [x[0]-h/2, x[-1]+h/2, y[0]-h/2, y[-1]+h/2]
    plt.figure(figsize=(6, 5))
    plt.imshow(V.T, origin="lower", extent=extent, aspect="equal")
    plt.colorbar(label="Potential V")
    if name == "dipole":
        plt.scatter([L/3, 2*L/3], [L/2, L/2], c="black", s=20)
        plt.contour(X, Y, V, levels=[0], colors="red", linewidths=1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.savefig(f"plots/{name}Heatmap.png", dpi=200)
    plt.close()
    plt.figure(figsize=(6, 5))
    contours = plt.contour(X, Y, V, levels=12)
    plt.clabel(contours, inline=True, fontsize=8)
    if name == "dipole":
        plt.contour(X, Y, V, levels=[0], colors="red", linewidths=2)
        plt.scatter([L/3, 2*L/3], [L/2, L/2], c=["red", "blue"], s=30)
    plt.xlim(0, L)
    plt.ylim(0, L)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.gca().set_aspect("equal")
    plt.tight_layout()
    plt.savefig(f"plots/{name}Contour.png", dpi=200)
    plt.close()
if __name__ == "__main__":
    for name in ("oneEdge", "fourEdge", "splitShell", "dipole", "poisson"):
        plot(name)
