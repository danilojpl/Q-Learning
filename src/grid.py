import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors 




def plot(grid):
    colors = np.array([[0,200,200,200],
                    [1,0,0,0],
                    [-1,255,153,0],
                    [100,63,165,76],
                    [200,255,0,0]])

    u, ind = np.unique(grid, return_inverse=True)
    b = ind.reshape((grid.shape))

    colors2 = colors[colors[:,0].argsort()][:,1:]/255.
    cmap = matplotlib.colors.ListedColormap(colors2)
    norm = matplotlib.colors.BoundaryNorm(np.arange(len(colors)+1)-0.5, len(colors))

    plt.imshow(b, cmap=cmap, norm=norm)
    plt.ion()
    plt.pause(1)


def melhorCaminho(recompensas,x,y): 
    prox = 0 
    grid = np.array ([[0,1,1,1,0,1,0,0,1,0],
                    [0,-1,0,0,0,0,0,-1,0,-1],
                    [0,1,1,0,1,1,0,0,0,1],
                    [0,0,0,0,0,0,1,1,0,1],
                    [1,-1,-1,1,0,-1,0,0,0,0],
                    [0,0,0,1,0,0,1,1,1,0],
                    [0,1,1,1,-1,0,1,1,-1,0],
                    [0,0,0,-1,1,0,-1,0,0,0],
                    [1,-1,0,0,0,0,0,0,0,1],
                    [-1,1,0,1,1,200,0,1,0,-1]])

    grid[x,y] = 100
    plot(grid)
    while (prox!=200):
        acao = max(recompensas[int(str(x)+str(y))].items(), key=lambda x: x[1])[0]
        if (acao == "cima"):
            grid[x,y] = 0
            prox = grid[x-1,y]
            grid[x-1,y] = 100
            x = x-1
        elif (acao == "baixo"):
            grid[x,y] = 0
            prox = grid[x+1,y]
            grid[x+1,y] = 100
            x = x+1
        elif (acao == "direita"):
            grid[x,y] = 0
            prox = grid[x,y+1]
            grid[x,y+1] = 100
            y = y+1
        elif (acao == "esquerda"):
            grid[x,y] = 0
            prox = grid[x,y-1]
            grid[x,y-1] = 100
            y = y-1
        plot(grid)
    plt.close()
        
