jogador = input("Digite seu apelido: ")

print("====================================")
print(f"  {jogador}, escolha seu lutador   ")
print("====================================")

print("Scorpion: especialista em ataques de fogo.")
print("Sub-Zero: especialista em ataques de gelo.")
print("Raiden: especialista em ataques elétricos.")
print("Liu Kang: especialista em ataques rápidos.")

while True:
    lutador = input(f"{jogador}, escolha seu lutador: ").lower()
    match lutador:
        case "scorpion":
            break
        case "sub-zero" | "subzero":
            break
        case "raiden":
            break
        case "liu kang":
            break
        case _:
            print("Personagem invalido!")

print("====================================")
print("         Dados Pré-partida          ")
print(f"            {jogador}              ")
print("====================================")

match lutador:
    case "scorpion":
        print("Lutador escolhido: Scorpion")
        print("Especialidade: Ataques de fogo")
    case "sub-zero" | "subzero":
        print("Lutador escolhido: Sub-Zero")
        print("Especialidade: Ataques de gelo")
    case "raiden":
        print("Lutador escolhido: Raiden")
        print("Especialidade: Ataques elétricos")
    case "liu kang":
        print("Lutador escolhido: Liu Kang")
        print("Especialidade: Ataques rápidos")
