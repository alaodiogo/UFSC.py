nome_poke = input("Qual e o nome do seu Pokémon? ")
xp_atual = float(input("Quanto de XP você possui? "))
xp_batalha = float(input("Quanto de XP você ganhou na batalha? "))
nivel_atual = 0

xp_total = xp_atual + xp_batalha

if xp_total >= 1000:
    nivel_atual += 1
    print(f"Parábens, {nome_poke} subiu de nível! Detalhes pós batalha: ")
    print(f"XP Antes da batalha: {xp_atual}")
    print(f"XP Ganho: {xp_batalha}")
    print(f"XP Total: {xp_total}")
    print(f"Nível atual: {nivel_atual}")
else:
    print("Detalhes Pós batalha:")
    print(f"XP Antes da batalha: {xp_atual}")
    print(f"XP Ganho: {xp_batalha}")
    print(f"XP Total: {xp_total}")
    print(f"Nível atual: {nivel_atual}")