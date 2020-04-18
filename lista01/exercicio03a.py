nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

soma = nota1 + nota2 + nota3 + nota4
media = soma / 4

print("A sua media foi de {} pontos.". format(round(media, 2)))