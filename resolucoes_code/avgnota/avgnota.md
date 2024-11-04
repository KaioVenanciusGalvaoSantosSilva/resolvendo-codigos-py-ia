# Documentação do Software: Calculadora de Média de Notas 📚

## Índice
- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Código Fonte](#código-fonte)
- [Exemplo de Uso](#exemplo-de-uso)
- [Considerações Finais](#considerações-finais)

## Descrição
Este software é uma aplicação simples em Python que permite ao usuário calcular a média aritmética de três notas fornecidas. O programa é interativo e fornece feedback imediato ao usuário com o resultado da média.

## Funcionalidades
- Solicita ao usuário que insira três notas.
- Calcula a média aritmética das notas inseridas.
- Exibe a média calculada de forma clara e legível.

## Tecnologias Utilizadas
- **Linguagem**: Python 3.x
- **Ambiente**: Qualquer ambiente que suporte Python (local ou online).

## Instalação
1. Certifique-se de que o Python 3.x esteja instalado em seu sistema.
2. Copie o código fonte para um arquivo com a extensão `.py`, por exemplo, `calcula_media.py`.

## Como Usar
1. Execute o script em um terminal ou console de Python.
2. Quando solicitado, insira as três notas, uma por vez.
3. Após inserir todas as notas, o programa calculará e exibirá a média.

## Código Fonte
```python
# Solicita ao usuário que insira três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Exibe o resultado da média
print("A média das notas é:", media)
```

# Exemplo de Uso

- Digite a primeira nota: 7.5
- Digite a segunda nota: 8.0
- Digite a terceira nota: 6.5
- A média das notas é: 7.333333333333333

## Considerações Finais
- Este software é destinado a fins educacionais e pode ser expandido para incluir mais funcionalidades, como validação de entrada e cálculo de outras estatísticas.
- Certifique-se de que as entradas sejam números válidos para evitar erros de execução.
- Sinta-se à vontade para modificar o código conforme necessário para atender às suas necessidades.