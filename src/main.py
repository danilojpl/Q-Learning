import numpy as np 
from config import GRID
from learning import Learning 
from agente import estadoTerminal
from grid import melhorCaminho 




aprender = Learning()
aprender.criarDicionario(GRID)
recompensas = aprender.calcPontuacao(GRID)

print ("digite a linha e coluna onde o carro está estacionado")
x = input("linha: ")
y = input("coluna: ")
while estadoTerminal(int(x),int(y),GRID):
    print ("vaga ocupada, digite novamente: ")
    x = input("linha: ")
    y = input("coluna: ")

while True:
    melhorCaminho(recompensas,int(x),int(y))
    print ("deseja testar em um novo local?:\ndigite 1 para sim ou 0 para finalizar o programa: ")
    resp = input()
    if (resp == "0"):
        break
    else:
        x = input("linha: ")
        y = input("coluna: ")

        	



