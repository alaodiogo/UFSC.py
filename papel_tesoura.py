import random
escolha_jogador = int(input("Escolha, 1- Pedra, 2- Papel e 3- Tesoura: "))
escolha_comp = random.randint(1, 3)

if escolha_jogador == escolha_comp:
    print("Empate!")
elif escolha_jogador == 1 and escolha_comp == 3:
    print("Você ganhou!")
elif escolha_jogador == 3 and escolha_comp == 1:
    print("Você perdeu!")
elif escolha_jogador == 3 and escolha_comp == 2:
    print("Você ganhou!")
elif escolha_jogador == 2 and escolha_comp == 3:
    print("Você perdeu!")
elif escolha_jogador == 2 and escolha_comp == 1:
    print("Vocẽ ganhou!")
elif escolha_jogador == 1 and escolha_comp == 2:
    print("Você perdeu!")