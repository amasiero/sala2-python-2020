notas = []
contador = 1
quantidade_notas = int(input("Informe a quantidade de notas que serão inseridas: "))

while(contador <= quantidade_notas):
  nota = float(input("Digite uma nota: "))
  notas.append(nota)
  contador += 1

soma = 0
for nota in notas:
  soma += nota

media = soma / len(notas)
print("A sua media foi de {} pontos.". format(round(media, 2)))