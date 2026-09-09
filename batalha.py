import random
vida_jogador = 20
vida_comp = 20

while True:
    vida_jogador -= random.randint(1, 6)
    if vida_jogador < 0:
        print("Você perdeu!")
        break
    vida_comp -= random.randint(1, 6)
    if vida_comp < 0:
        print("Você ganhou!")
        break