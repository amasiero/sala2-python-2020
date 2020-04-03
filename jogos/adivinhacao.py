import random

def jogar():
  print("***********************************")
  print("  Bem-vindo ao Jogo da Advinhação  ")
  print("***********************************")

  numero_secreto = random.randint(1, 100)

  while True:
    print("Qual nível você deseja participar?")
    print("(1) facil (2) normal (3) dificil")
    nivel = int(input("Escolha seu nivel: "))

    if nivel == 1 or nivel == 2 or nivel == 3:
      break
      
    print("O nivel deve ser escolhido entre as opcoes apresentadas.")

  tentativa = 1
  max_tentativas = 0

  if nivel == 1:
      max_tentativas = 30
  elif nivel == 2:
      max_tentativas = 15
  elif nivel == 3:
      max_tentativas = 5

  while tentativa <= max_tentativas:
      print("Tentativa {} de {}.".format(tentativa, max_tentativas))
      numero_escolhido = input("Escolha um número entre 1 e 100: ")
      numero_escolhido = int(numero_escolhido)

      if numero_escolhido < 1 or numero_escolhido > 100:
          print("Abestado! Só aceito valores entre 1 e 100.")
          continue

      acertou = numero_secreto == numero_escolhido
      maior = numero_secreto > numero_escolhido
      menor = numero_secreto < numero_escolhido

      if acertou:
          print("Uhuuuuu!!!")
          print("Parabéns!!!!!")
          print("Voce eh foooogoooo =D")
          break
      else:
          print("Errrrooooouuuuu!!!! =(")
          if maior:
              print("O numero secreto é maior que o escolhido.")
          elif menor:
              print("O numero secreto é menor que o escolhido.")

      tentativa = tentativa + 1

  if tentativa > max_tentativas:
    print("O numero secreto era {}.".format(numero_secreto))
  print("Fim do Jogo")