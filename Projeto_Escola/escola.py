print("###### ESCOLA STARK ######")
turma = []

while True:
    nome = input("Digite o nome do aluno: ")
    if not nome:
        break

    notas = []
    for i in range(3):  # 0, 1, 2
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    aluno = (nome, notas)
    turma.append(aluno)

media_dos_alunos = []
for aluno in turma:
    print("-" * 40)
    nome = aluno[0]
    notas = aluno[1]

    print(f"Nome: {nome}")
    print(f"Nota 1: {notas[0]:.1f}")
    print(f"Nota 2: {notas[1]:.1f}")
    print(f"Nota 3: {notas[2]:.1f}")

    menor_nota = min(notas)
    indice_menor_nota = notas.index(menor_nota)
    notas.pop(indice_menor_nota)
    print(f"A nota descartada foi a nota {indice_menor_nota + 1}.")

    if notas[0] < notas[1]:
        media = (notas[0] * .4) + (notas[1] * .6)
    else:
        media = (notas[1] * .4) + (notas[0] * .6)

    print(f"Sua média foi de {media:.1f} pontos.")

    media_dos_alunos.append(media)
    print("-" * 40)

media_da_turma = sum(media_dos_alunos) / len(media_dos_alunos)

media_por_aluno = []
for aluno, media in zip(turma, media_dos_alunos):
    media_por_aluno.append((aluno[0], media))

media_por_aluno.sort(key=lambda aluno: aluno[1])

print("-" * 40)
print(f"Média da turma: {media_da_turma:.1f}")
print(f"Top 1: {media_por_aluno[-1][0]}")
print(f"Top 2: {media_por_aluno[-2][0]}")
print(f"Top 3: {media_por_aluno[-3][0]}")

contador_alunos = sum(media > media_da_turma for media in media_dos_alunos)

print(f"Estão acima da média da turma {contador_alunos} alunos.")
print("-" * 40)

print("FIM DO PROGRAMA")
