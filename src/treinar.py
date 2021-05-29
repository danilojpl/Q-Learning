import agente
import config 


class Treinar:
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
            dictPontos["cima"] = 0
            dictPontos["baixo"] = 0
            dictPontos["direita"] = 0
            dictPontos["esquerda"] = 0
            self.estado[i] = dictPontos
    
    def qLearning(self,x, y, movimento,xprox, yprox ,recompensa):
        prox = int(str(xprox)+str(yprox))
        posicao = int(str(x)+str(y))
        qValue = self.estado[posicao][movimento]+self.alfa*(
                                                        recompensa+self.gama*self.estado[prox].get(
                                                        sorted(self.estado[prox].keys(), 
                                                        key=lambda x: self.estado[prox][x])[-1] )-
                                                        self.estado[posicao][movimento])
        return qValue


    def calcPontuacao(self, grid):
        print ("Treinando...")
        for faseTreinamento in range(50000):
            linha, coluna = agente.localInicio(grid)
            while not agente.estadoTerminal(linha,coluna, grid):
                acao = agente.novoMovimento(linha, coluna,self.estado, grid)

                antLinha = linha 
                antColuna = coluna 
                linha, coluna = agente.novoLocal(linha, coluna, acao)

                recompensa = grid[linha,coluna]
                antQvalue = self.estado[int(str(antLinha)+str(antColuna))][acao]
                qValue = self.qLearning(antLinha, antColuna, acao, linha, coluna, recompensa)
                self.estado[int(str(antLinha)+str(antColuna))][acao] = qValue
        print ("Treinamento Finalizado")        
        return self.estado 
        

    



        




    

    
