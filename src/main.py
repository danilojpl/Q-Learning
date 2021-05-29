from config import GRID
from treinar import Treinar 
from agente import estadoTerminal
from grid import melhorCaminho

def escolher():
    x = input("linha: ")
    y = input("coluna: ")
    while estadoTerminal(int(x),int(y),GRID):
        print ("vaga ocupada, digite novamente: ")
        x = input("linha: ")
        y = input("coluna: ")
    return x, y

aprender = Treinar()
aprender.criarDicionario(GRID)
recompensas = aprender.calcPontuacao(GRID)

print ("digite a linha e coluna onde o carro está estacionado")
x, y = escolher()

while True:
    melhorCaminho(recompensas,int(x),int(y))
    print ("deseja testar em um novo local?:\ndigite 1 para sim ou qualquer outra tecla para finalizar o programa: ")
    resp = input()
    if (resp == "1"):
        x, y = escolher()
    else:
        break
        
  
            

        	



