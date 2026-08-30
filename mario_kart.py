jogador = input("Digite seu apelido: ")
posicao = int(input("Qual é sua posição final na corrida? "))

print(f"{jogador}, você ganhou em {posicao}º lugar, parabéns!!!" \
      if posicao == 1 else f"{jogador}, infelizmente você perdeu em {posicao}º lugar :(")
