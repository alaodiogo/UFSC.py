notas = [float(x) for x in input().split()]

notas.remove(min(notas)) and notas.remove(max(notas))

total_nota = sum(notas)

print (round(total_nota, 1))  