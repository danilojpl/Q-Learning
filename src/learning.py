import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import config



class Learning:

    def __init__(self):
        self.estado = config.MOVIMENTOS
        self.alfa = config.ALFA
        self.gama = config.GAMA
        self.branco = config.RECOMPENSAS.get("branco")
        self.atropelar = config.RECOMPENSAS.get("atropelar")
        self.bater = config.RECOMPENSAS.get("bater")
        self.destino = config.RECOMPENSAS.get("destino")

    def criarDicionario(self, grid):
        for i in range(len(grid)*10):
            dictPontos = {} 
            # dictPontos[str(i)] = 0
            dictPontos["cima"] = 0
            dictPontos["baixo"] = 0
            dictPontos["direita"] = 0
            dictPontos["esquerda"] = 0
            self.estado[i] = dictPontos
        # print("teste")
    
    # def qLearning(self, posicao ,movimento, grid):
    #     for movimento in self.dictPontos:
    #         if ()

    #          self.estado[int(str(i)+str(j))]["baixo"] = self.estado[int(str(i)+str(j))]["baixo"]+self.alfa*(
    #                 self.branco+self.gama*self.estado[int(str(i)+str(j))+1].get(
    #                 sorted(self.estado[int(str(i)+str(j))+1].keys(), key=lambda x: self.estado[int(str(i)+str(j))+1][x])[-1] )-self.estado[int(str(i)+str(j))]["baixo"])


    def calcPontuacao(self, grid):
        for i in range (len(grid)):
            for j in range (len(grid)):
                if (grid[i+1][j] == 0):
                    self.estado[int(str(i)+str(j))]["baixo"] = self.estado[int(str(i)+str(j))]["baixo"]+self.alfa*(
                    self.branco+self.gama*self.estado[int(str(i)+str(j))+1].get(
                    sorted(self.estado[int(str(i)+str(j))+1].keys(), key=lambda x: self.estado[int(str(i)+str(j))+1][x])[-1] )-self.estado[int(str(i)+str(j))]["baixo"])

    



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

aprender = Learning()
aprender.criarDicionario(grid)
aprender.calcPontuacao(grid)
        	
        




    

    
