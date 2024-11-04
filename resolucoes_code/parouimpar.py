## 4 - Verificando Números Pares e Ímpares 🧮

# Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
# Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

# O que aprenderemos?
# * Utilização de condicionais em Python (if, else) para realizar verificações.
# * Introdução ao conceito de operador de módulo (%) para verificar se um número é par ou ímpar.
# * Exploração do uso de uma ferramenta de IA, como o Github Copilot, para otimizar a estrutura do código.


# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")