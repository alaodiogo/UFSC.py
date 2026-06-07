while True:
    mary = 0
    john = 0
    numero_de_jogadas = int(input())
    if numero_de_jogadas == 0:
            break
    resultados_das_jogadas = [int(w) for w in input().split()]
    for jogada_atual in resultados_das_jogadas:
        match jogada_atual:
            case 0:
                mary += 1
            case 1:
                john += 1
    print (f" Mary won {mary} times and John won {john} times")