# Documentação do Software: Verificador de Palíndromos

## Descrição
Este software é uma aplicação simples que verifica se uma palavra fornecida pelo usuário é um palíndromo. Um palíndromo é uma palavra que permanece a mesma quando lida de trás para frente.

## Funcionalidades
- Solicita ao usuário que insira uma palavra.
- Inverte a palavra inserida.
- Compara a palavra original com a palavra invertida.
- Informa ao usuário se a palavra é um palíndromo ou não.

## Tecnologias Utilizadas
- Python 3.x

## Como Usar
1. Execute o script Python.
2. Quando solicitado, digite uma palavra.
3. O programa irá informar se a palavra é um palíndromo.

## Código
```python
# Solicita ao usuário que insira uma palavra
palavra = input("Digite uma palavra: ")

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se a palavra é um palíndromo
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
```

## Exemplos de Uso
- **Entrada:** `arara`
  - **Saída:** A palavra 'arara' é um palíndromo.
  
- **Entrada:** `python`
  - **Saída:** A palavra 'python' não é um palíndromo.

## Considerações Finais
Este software é uma introdução ao conceito de palíndromos e à manipulação de strings em Python. É uma ótima maneira de praticar a lógica de programação e o uso de condicionais.

## Licença
Este projeto é de domínio público e pode ser utilizado, modificado e distribuído livremente.