class Aluno:
    def __init__(self, nome, nota_prova_1=0.0, nota_prova_2=0.0):
        self.nome = nome
        self.nota_prova_1 = nota_prova_1
        self.nota_prova_2 = nota_prova_2

    def calcula_media(self):
        return (self.nota_prova_1 + self.nota_prova_2) / 2

    def estah_aprovado(self):
        return self.calcula_media() >= 7

    def __str__(self):
        return self.nome


alunos = [
    Aluno('Lorena', 7, 9),
    Aluno('Samuel', 8, 6),
    Aluno('Cayo', 9, 7),
    Aluno('Samantha', 8, 7),
    Aluno('Joao Pedro', 10, 10),
    Aluno('Matias', 0.1, 10),
    Aluno('Oquendo', 7, 8.5),
    Aluno('Pardim', 9, 8.5)
]


for aluno in alunos:
    print(f'{aluno.nome} teve a média de {aluno.calcula_media()} pontos.'
          f' Com essa média está {"aprovado." if aluno.estah_aprovado() else "REPROVADO!"}')
