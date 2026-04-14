num_competidores, qtd_total_folhas, qtd_folhas_competidor = [int(w) for w in input().split()]

o_papel_e_suficiente = qtd_total_folhas // num_competidores // qtd_folhas_competidor

if o_papel_e_suficiente > 0:
    print ("S")
else:
    print ("N")
