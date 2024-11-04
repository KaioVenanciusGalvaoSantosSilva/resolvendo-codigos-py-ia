
# ## 5 - Calculando Média de Notas 📚

# Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. 
# Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

# O que aprenderemos?
# * Uso de variáveis para armazenar dados fornecidos pelo usuário.
# * Aplicação de operadores aritméticos (+, /) para calcular a média de um conjunto de valores.
# * Prática na solicitação e manipulação de entrada do usuário.

# Solicita ao usuário que insira três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Exibe o resultado da média
print("A média das notas é:", media)