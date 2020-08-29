# Exercicio 1
with open('arquivo.txt', 'r') as arquivo:
    total_linhas = len(arquivo.readlines())
    print(f'O arquivo possui um total de {total_linhas} linhas.')
    # Solução do Rafa
    # print(sum(1 for linha in arquivo))

# Exercicio 2
with open('arquivo.txt', 'r') as arquivo:
    quantidade_vogais = 0
    for linha in arquivo:
        quantidade_vogais += len([letra for letra in linha if letra in 'aeiou'])
    print(f'O total de vogais é {quantidade_vogais}.')

# Exercicio 3
with open('arquivo.txt', 'r') as arquivo:
    quantidade_consoantes = 0
    quantidade_vogais = 0
    for linha in arquivo:
        quantidade_vogais += len([letra for letra in linha if letra in 'aeiou'])
        quantidade_consoantes += len([letra for letra in linha if letra in 'bcdfghjklmnpqrstvwyxz'])
    print(f'O total de vogais é {quantidade_vogais} e a de consoantes é {quantidade_consoantes}.')

# Exercicio 4
with open('arquivo.txt', 'r') as arquivo:
    caracter = input('Informe um caracter: ')
    letras = 0
    for linha in arquivo:
        letras += len([letra for letra in linha if letra == caracter])
    print(f'Total de {caracter} é {letras}.')

# Exercicio 5
with open('arquivo.txt', 'r') as arquivo:
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    letras = [0 for letra in alfabeto]
    for linha in arquivo:
        for indice, letra in zip(range(len(alfabeto)), alfabeto):
            letras[indice] += linha.count(letra)

    resultado = 'Total de: '
    for letra, quantidade in zip(alfabeto, letras):
        resultado += f'{letra}:{quantidade} '
    print(resultado)

# Exercício 6
# Solucao 1
with open('arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        texto = (linha.strip().replace('a', '*')
                 .replace('e', '*')
                 .replace('i', '*')
                 .replace('o', '*')
                 .replace('u', '*'))
        print(texto)

# Solucao 2
import re
with open('arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        texto = re.sub(r'[aeiou]', '*', linha.strip())
        print(texto)

# Exercício 7
origem = input('Digite o arquivo de origem: ')
destino = input('Digite o arquivo de destino: ')

with open(origem, 'r') as leitura:
    with open(destino, 'w') as escrita:
        for linha in leitura:
            escrita.write(linha.upper())
