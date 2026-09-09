import random
vitorias_jogador = 0
vitorias_comp = 0

while True:
    escolha_jogador = int(input("Escolha, 1- Pedra, 2- Papel e 3- Tesoura: "))
    escolha_comp = random.randint(1, 3)
    
    if escolha_jogador == escolha_comp:
        print("Empate!")
    elif escolha_jogador == 1 and escolha_comp == 3:
        print("Você ganhou!")
        vitorias_jogador += 1
    elif escolha_jogador == 2 and escolha_comp == 1:
        print("Você ganhou!")
        vitorias_jogador += 1
    elif escolha_jogador == 3 and escolha_comp == 2:
        print("Vocẽ ganhou!")
        vitorias_jogador += 1
    else:
        print("Você perdeu!")
        vitorias_comp += 1
    
    if vitorias_jogador == 3:
        print("Você ganhou a disputa!")
        break
    elif vitorias_comp == 3:
        print("Você perdeu a disputa")
        break
        