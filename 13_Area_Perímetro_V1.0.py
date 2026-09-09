import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep (0.5)

print("=================================")
print("Á R E A  E  P E R Í M E T R O")
print("=================================")

largura = float(input("Digite a largura do retângulo: "))  # Recebe a largura e guarda na variável largura
altura = float(input("Digite a altura do retângulo: "))    # Recebe a altura e guarda na variável altura

area = largura * altura                                    # Calcula a área do retângulo
perimetro = 2 * (largura + altura)                         # Calcula o perímetro do retângulo

print("Área:", area)                                       # Mostra a área na tela
print("Perímetro:", perimetro)                             # Mostra o perímetro na tela