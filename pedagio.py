total_rodovia, distancia_pedagios = [int(w) for w in input().split()]
custo_km, valor_pedagios = [int(w) for w in input().split()]

total_de_pedagios = total_rodovia//distancia_pedagios
valor_total_pedagios = valor_pedagios*total_de_pedagios
custo_por_km = custo_km*total_rodovia

gasto_total = valor_total_pedagios+custo_por_km

print(gasto_total)
