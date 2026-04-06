xicara_trigo, ovos, colher_leite = [int(w) for w in input().split()]

bolos_trigo = xicara_trigo // 2
bolos_ovo = ovos // 3
bolos_colher_leite = colher_leite // 5

quantidade_bolo = min(bolos_trigo, bolos_ovo, bolos_colher_leite)

print (quantidade_bolo)