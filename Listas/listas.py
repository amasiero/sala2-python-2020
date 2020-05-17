numeros = [] # inicializo a lista
numeros.append(1) # adiciono numero ao final da lista
print(numeros)
numeros.append(2)
print(numeros)
numeros.insert(0, 0) # adiciono numero em uma posicao especifica
print(numeros) 
print('tamanho da lista', len(numeros)) # tamanho da lista
print(numeros[1]) # consulto um valor na lista

letras = ['a', 'b', 'd', 'e', 'f']
print(letras)
letras.insert(2, 'c')
print(letras)

fatiado = letras[2:4] 
# comeca na posicao 2 e exibe o numero de elementos de acordo
# com o resultado da diferenca entre 4 (fim) e 2 (inicio) 
print(fatiado)

fatiado = letras[2:]
print(fatiado)

fatiado = letras[:4]
print(fatiado)

fatiado = letras[1:7:2]
print(fatiado)

print(letras[-1])

print(letras[::-1]) # inverção da lista

fatiado = letras[7:0:-2]
print(fatiado)

fatiado = letras[1::2]
print(fatiado)

# Exercicio 01

numeros = [10, 29, 83, 15, 5]

# opcao 1
for indice in range(len(numeros)):
	print(numeros[indice])

# opcao 2
for numero in numeros:
	print(numero)

# Exercicio 02

numerosReais = [3.5, 9.5, 9.2, 10.0, 10.0, 10.0, 7.11, 10.0, 8.0, 9.0]

for numeroReal in numerosReais[::-1]:
	print(numeroReal)

# Exercicio 03

notas = []
indice = 0

while(indice < 4):
	notas.append(float(input("Informe uma nota: ")))
	indice += 1

print('Notas:',notas)
soma = 0
for nota in notas:
	soma += nota # soma = soma + nota
print(f'Média: {(soma/len(notas)):.1f}')

print(f'Média: {(sum(notas)/len(notas)):.1f}')