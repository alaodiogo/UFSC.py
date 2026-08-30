jogador = input("Digite seu apelido: ")

print("====================================")
print(f"  {jogador}, escolha sua função    ")
print("====================================")

print("Tripulante: Deve realizar tarefas e descobrir quem é o impostor.")
print("Impostor: Deve eliminar os tripulantes sem ser descoberto.")
print("Engenheiro: Pode utilizar as entradas de ventilação para se movimentar pelo mapa.")
print("Cientista: Pode acompanhar informações dos jogadores através de seu painel.")

while True:
    funcao = input(f"{jogador}, escolha sua função: ").lower()
    match funcao:
        case "tripulante":
            break
        case "impostor":
            break
        case "engenheiro":
            break
        case "cientista":
            break
        case _:
            print("Função invalida!")
            
print("====================================")
print(f"  {jogador}, escolha um mapa       ")
print("====================================")

print("The Skeld")
print("MIRA HQ")
print("Polus")
print("The Airship")

while True:
    mapa = input(f"{jogador}, escolha um mapa: ").lower()
    match mapa:
        case "the skeld":
            break
        case "mira hq":
            break
        case "polus":
            break
        case "the airship":
            break
        case _:
            print("Mapa invalido!")

print("====================================")
print("         Dados Pré-partida          ")
print(f"            {jogador}              ")
print("====================================")

match funcao:
    case "tripulante":
        print("Função escolhida: Tripulante")
        print("Objetivo: Deve realizar tarefas e descobrir quem é o impostor.")
    case "impostor":
        print("Função escolhida: Impostor")
        print("Objetivo: Deve eliminar os tripulantes sem ser descoberto.")
    case "engenheiro":
        print("Função escolhida: Engenheiro")
        print("Papel: Pode utilizar as entradas de ventilação para se movimentar pelo mapa.")
    case "cientista":
        print("Função escolhida: Cientista")
        print("Papel: Pode acompanhar informações dos jogadores através de seu painel.")
    
match mapa:
    case "the skeld":
        print("Mapa escolhido: The Skeld")
    case "mira hq":
        print("Mapa escolhido: MIRA HQ")
    case "polus":
        print("Mapa escolhido: Polus")
    case "the airship":
        print("Mapa escolhido: The Airship")    