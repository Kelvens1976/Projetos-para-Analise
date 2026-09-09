import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela ()
time.sleep (0.5)

celsius = float(input("Digite a temperatura em Celsius: "))  # Recebe a temperatura em Celsius

print("==================================================")
print("C O N V E R S O R  D E  T E M P E R A T U R A S")
print("==================================================")

fahrenheit = (celsius * 9 / 5) + 32                        # Converte Celsius para Fahrenheit usando a fórmula de conversão

print("Temperatura em Fahrenheit:", fahrenheit)            # Mostra a temperatura convertida