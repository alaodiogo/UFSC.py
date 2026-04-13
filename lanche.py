codigo_lanche, quanti_lanche = [int(w) for w in input().split()]

match codigo_lanche:
    case 1:
        lanche = 4.00
    case 2:
        lanche = 4.50
    case 3:
        lanche = 5.00
    case 4:
        lanche = 2.00
    case 5:
        lanche = 1.50
        
total = lanche * quanti_lanche

print (total)