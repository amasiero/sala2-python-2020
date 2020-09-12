# Exercicio 01
def exibe_piramide_numeros(n):
    for linha in range(1, n + 1):
        for numero in range(linha):
            print(linha, end=' ')
        print()


# Exercicio 02
def exibe_piramide_numeros_contagem(n):
    for linha in range(1, n + 1):
        for numero in range(1, linha + 1):
            print(numero, end=' ')
        print()


exibe_piramide_numeros_contagem(10)


# Exercicio 03
def soma(a, b, c):
    print(a + b + c)


soma(1, 2, 3)
