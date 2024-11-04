# Documentação de Software: Repetição de Strings

## 1. Descrição do Software

Este software é um programa simples em Python que solicita ao usuário uma string e um número inteiro, e retorna a string repetida o número de vezes especificado. O objetivo é ensinar conceitos básicos de manipulação de strings e entrada de dados.

## 2. Funcionalidades

- Solicita ao usuário que insira uma string.
- Solicita ao usuário que insira um número inteiro.
- Retorna a string repetida o número de vezes indicado pelo usuário.
- Exibe o resultado na tela.

## 3. O que aprenderemos?

- Manipulação de Strings (`string`).
- Números Inteiros (`int`).
- Múltiplas repetições de strings.
- Entrada de dados do usuário.
- Uso de sugestões de código (como as do GitHub Copilot).

## 4. Estrutura do Código

```python
# Solicita ao usuário que insira uma string
texto = input("Digite uma string: ")

# Solicita ao usuário que insira um número inteiro
repeticoes = int(input("Digite um número inteiro: "))

# Retorna a string repetida o número de vezes informado
resultado = texto * repeticoes

# Exibe o resultado
print("A string repetida é:", resultado)

## 5. Como Usar

- Execute o programa em um ambiente Python.
- Quando solicitado, insira uma string de sua escolha.
- Em seguida, insira um número inteiro que representa quantas vezes você deseja repetir a string.
- O programa exibirá a string repetida conforme o número fornecido.

## 6. Exemplos de Uso

### Exemplo 1:
- **Entrada:**
  - String: "Olá"
  - Número: 3
- **Saída:** 
  - "A string repetida é: OláOláOlá"

### Exemplo 2:
- **Entrada:**
  - String: "Python"
  - Número: 2
- **Saída:** 
  - "A string repetida é: PythonPython"

## 7. Considerações Finais

Este programa é uma ótima maneira de praticar a entrada de dados e a manipulação de strings em Python. É simples, mas eficaz para entender como as repetições de strings funcionam na linguagem.