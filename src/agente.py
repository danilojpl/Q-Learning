import numpy as np

def estadoTerminal(x, y, grid):
    if (grid[x,y] == 100):
        return False 
    else:
        return True


def localInicio(grid):
    linha = np.random.randint(len(grid))
    coluna = np.random.randint(len(grid))
    
    while estadoTerminal(linha, coluna, grid):
        linha = np.random.randint(len(grid))
        coluna = np.random.randint(len(grid))
    return linha,coluna


def novoMovimento(x, y, estado,grid):
    indice = int(str(x)+str(y))
    if (np.random.randint(100)>5):
        return max(estado[indice].items(), key=lambda x: x[1])[0]
         
    else:
        aleatorio = np.random.randint(4)
        if (aleatorio == 0):
            return "cima"
        elif (aleatorio == 1):
            return "baixo"
        elif (aleatorio == 2):
            return "direita"
        elif (aleatorio == 3):
            return "esquerda"


def novoLocal(x,y,movimento):

    if (movimento == "cima"):
        if (x-1<0):
            x = x
        else: 
            x-=1
    elif (movimento == "baixo"):
        if (x+1>9):
            x = x
        else: 
            x+=1
    elif (movimento == "direita"):
        if (y+1>9):
            y = y
        else: 
            y+=1
    elif (movimento == "esquerda"):
        if (y-1<0):
            y = y
        else: 
            y-=1

    return x, y


    
    


            
    
