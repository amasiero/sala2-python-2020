
def jogar():
  print("***********************************")
  print("    Bem-vindo ao Jogo da Forca     ")
  print("***********************************")

  palavra_secreta = "banana"

  enforcou = False
  acertou = False

  #enquanto nao enforcou e nao acertou
  while not enforcou and not acertou:
    chute = input("Fale uma letra: ")
    chute = chute.strip()

    indice = 0
    for letra in palavra_secreta:
      if chute.upper() == letra.upper():
        print("Encontrei a letra {} na posição {}.".format(letra, indice))
      indice = indice + 1


  print("Fim de jogo.")

    