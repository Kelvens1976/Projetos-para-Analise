import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep (3)

print("============================================")
print("A N T E C E S S O R   E   S U C E S S O R")
print("============================================")

numero = int(input("Digite um número inteiro: "))  # Recebe um número inteiro e guarda na variável numero

antecessor = numero - 1                            # Calcula o número que vem antes
sucessor = numero + 1                              # Calcula o número que vem depois

print("Antecessor:", antecessor)                   # Mostra o antecessor na tela
print("Sucessor:", sucessor)                       # Mostra o sucessor na tela