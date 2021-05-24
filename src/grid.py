import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors 

grid = np.array ([[0,1,1,1,0,1,0,0,1,0],
                [0,-1,0,0,0,0,0,-1,0,-1],
                [0,1,1,0,1,1,0,0,0,1],
                [0,0,0,0,0,0,1,1,0,1],
                [1,-1,-1,1,0,-1,100,0,0,0],
                [0,0,0,1,0,0,1,1,1,0],
                [0,1,1,1,-1,0,1,1,-1,0],
                [0,0,0,-1,1,0,-1,0,0,0],
                [1,-1,0,0,0,0,0,0,0,1],
                [-1,1,0,1,1,200,0,1,0,-1]])

colors = np.array([[0,200,200,200],
                [1,170,255,245],
                [-1,208,130,40],
                [100,63,165,76],
                [200,255,255,255]])

u, ind = np.unique(grid, return_inverse=True)
b = ind.reshape((grid.shape))

colors2 = colors[colors[:,0].argsort()][:,1:]/255.
cmap = matplotlib.colors.ListedColormap(colors2)
norm = matplotlib.colors.BoundaryNorm(np.arange(len(colors)+1)-0.5, len(colors))

plt.imshow(b, cmap=cmap, norm=norm)

cb = plt.colorbar(ticks=np.arange(len(colors)))
cb.ax.set_yticklabels(np.unique(colors[:,0]))

plt.show()


grid = np.array ([[0,1,1,1,0,1,0,0,1,0],
                [0,-1,0,0,0,0,0,-1,0,-1],
                [0,1,1,0,1,1,0,0,0,1],
                [0,0,0,0,0,0,1,1,0,1],
                [1,-1,-1,1,0,-1,100,0,0,0],
                [0,0,0,1,0,0,1,1,1,0],
                [0,1,1,1,-1,0,1,1,-1,0],
                [0,0,0,-1,1,0,-1,0,0,0],
                [1,-1,0,0,0,0,0,0,0,1],
                [-1,1,0,1,1,200,0,1,0,-1]])

colors = np.array([[0,200,200,200],
                [1,170,255,245],
                [-1,208,130,40],
                [100,63,165,76],
                [200,255,255,255]])

u, ind = np.unique(grid, return_inverse=True)
b = ind.reshape((grid.shape))

colors2 = colors[colors[:,0].argsort()][:,1:]/255.
cmap = matplotlib.colors.ListedColormap(colors2)
norm = matplotlib.colors.BoundaryNorm(np.arange(len(colors)+1)-0.5, len(colors))

plt.imshow(b, cmap=cmap, norm=norm)

cb = plt.colorbar(ticks=np.arange(len(colors)))
cb.ax.set_yticklabels(np.unique(colors[:,0]))

plt.show()
                