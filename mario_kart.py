jogador = input("Digite seu apelido: ")
posicao = int(input("Qual é sua posição final na corrida? "))

print(f"Você ganhou em {posicao}º lugar, parabéns!!!" if posicao == 1 else f"Infelizmente você perdeu em {posicao}º lugar :(")