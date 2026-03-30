area = int(input())

litro = 3.6 # Total do galão de tinta
cober_litro = 18 # Total da cobertura de tinta
preco_galao = 25

rendi_galao = litro*cober_litro # Calculo para saber o total de rendimento do galão de tinta
total_galoes = max(round(area/rendi_galao), 1) # Calculo para saber o total de galões necessarios
preco_total = total_galoes*preco_galao

print (f"- área de cobertura: {area}")
print (f"- número de galões: {total_galoes}")
print (f"- valor a ser pago: R$ {preco_total}.00")