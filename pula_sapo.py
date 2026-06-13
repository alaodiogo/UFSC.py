tamanho_pulo_sapo, qtdade_canos = [int(x) for x in input().split()]
alturas = [int(x) for x in input().split()]

posicao_atual = 0
proxima_posicao = 1

for _ in range(qtdade_canos - 1):
    sapo_pula = abs(alturas[posicao_atual] - alturas[proxima_posicao])
    if sapo_pula > tamanho_pulo_sapo:
        resultado = 'GAME OVER'
        break
    else:
        resultado = 'YOU WIN'
    posicao_atual = posicao_atual + 1 #Para percorrer a lista usando os indices
    proxima_posicao = proxima_posicao + 1 #Para percorrer a lista usando os indices
    
print (resultado)