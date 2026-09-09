import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep (0.5)

print("===============================")
print("M É D I A  D E  N O T A S")
print("===============================")

nota1 = float(input("Digite a primeira nota: "))       # Recebe a primeira nota e guarda na variável nota1
nota2 = float(input("Digite a segunda nota: "))        # Recebe a segunda nota e guarda na variável nota2
nota3 = float(input("Digite a terceira nota: "))       # Recebe a terceira nota e guarda na variável nota3

media = (nota1 + nota2 + nota3) / 3                    # Soma as três notas e divide o resultado por 3

print("Primeira nota:", nota1)                         # Mostra a primeira nota na tela
print("Segunda nota:", nota2)                          # Mostra a segunda nota na tela
print("Terceira nota:", nota3)                         # Mostra a terceira nota na tela
print(f"Média: {media:.2f}")                           # Mostra a média calculada na tela