# Documentação de Software: Verificação de Números Pares e Ímpares

## 1. Visão Geral

Este software é uma aplicação simples em Python que permite ao usuário verificar se um número inteiro fornecido é par ou ímpar. O programa utiliza condicionais e o operador de módulo (%) para realizar essa verificação.

## 2. Objetivos

- Receber um número inteiro do usuário.
- Determinar se o número é par ou ímpar.
- Exibir o resultado para o usuário.

## 3. Tecnologias Utilizadas

- **Linguagem de Programação**: Python 3.x
- **Ambiente de Desenvolvimento**: Qualquer IDE ou editor de texto que suporte Python (ex: PyCharm, VSCode, Jupyter Notebook).

## 4. Requisitos

- Python 3.x instalado no sistema.
- Acesso a um terminal ou console para executar o script.

## 5. Instalação

1. Certifique-se de que o Python 3.x está instalado em seu sistema.
2. Copie o código fornecido para um arquivo com a extensão `.py`, por exemplo, `verifica_par_impar.py`.
3. Abra um terminal e navegue até o diretório onde o arquivo foi salvo.

## 6. Uso

Para executar o programa, utilize o seguinte comando no terminal:

```bash
python verifica_par_impar.py 
O programa solicitará que o usuário insira um número inteiro. Após a inserção, ele verificará se o número é par ou ímpar e exibirá o resultado.
```
- **Exemplo de Execução**

- Digite um número inteiro: 4
- O número é par.

# 7. Estrutura do Código
O código é estruturado da seguinte maneira:

- Solicita ao usuário que insira um número inteiro
- numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar

```
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

**Explicação do Código**
- input(): Função que solicita a entrada do usuário.
- int(): Converte a entrada para um número inteiro.
- if numero % 2 == 0: Condicional que verifica se o número é divisível por 2 (número par).
- print(): Exibe o resultado ao usuário.

## 8. Considerações Finais
Este software é um exemplo básico de como utilizar condicionais em Python e o operador de módulo para realizar verificações. É uma boa prática para iniciantes aprenderem sobre lógica de programação e manipulação de entradas do usuário.

## 9. Contribuições
Contribuições para melhorias ou otimizações do código são bem-vindas. Sinta-se à vontade para sugerir melhorias ou correções.

## 10. Licença
Este software está disponível para uso e modificação. Consulte o arquivo de licença para mais informações.