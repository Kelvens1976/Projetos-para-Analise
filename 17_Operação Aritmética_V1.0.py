import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.7)    

numero1 = int(input("Digite o primeiro número: "))       # Recebe o primeiro número inteiro, por isso o "int"
numero2 = int(input("Digite o segundo número: "))        # Recebe o segundo número inteiro, por isso o "int"

soma = numero1 + numero2                                # Calcula a soma dos dois números => leia-se soma receberá num1 + num2
subtracao = numero1 - numero2                            # Calcula a subtração dos dois números => leia-se subtração receberá num1 - num2
multiplicacao = numero1 * numero2                        # Calcula a multiplicação dos dois números => leia-se multiplicação receberá num1 * num2

print("Soma:", soma)                                     # Apresenta o resultado da soma, armazenado na variável soma
print("Subtração:", subtracao)                           # Apresenta o resultado da subtração, armazenado na variável subtração
print("Multiplicação:", multiplicacao)                   # Apresenta o resultado da multiplicação, armazenado na variável multiplicação

if numero2 != 0:                                         # Verifica se o segundo número é diferente de zero => leia-se, se num2 for diferente (!=) 0, faça
    divisao = numero1 / numero2                           # Calcula a divisão => leia-se divisão receberá num1 / num2
    print("Divisão:", divisao)                            # Apresenta o resultado da divisão 
else:                                                    # Executado quando o segundo número é zero => leia-se, senão .....
    print("Não é possível dividir por zero.")            # Informa que a divisão não pode ser realizada