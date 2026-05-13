salario = float(input())

#Tabela de percentual de ajuste (Aqui para possiveis ajustes futuros)
percentual_1 =  0.15 # 15%
percentual_2 = 0.12 # 12%
percentual_3 = 0.1 # 10%
percentual_4 = 0.07 # 7%
percentual_5 = 0.04 # 4% 

if 0 < salario == 400.00:
    reajuste = salario * percentual_1
    em_percentual = "15 %"
elif 400.01 <= salario <= 800.00:
    reajuste = salario * percentual_2
    em_percentual = "12 %"
elif 800.01 <= salario <= 1200.00:
    reajuste = salario * percentual_3
    em_percentual = "10 %"
elif 1200.01 <= salario <= 2000.00:
    reajuste = salario * percentual_4
    em_percentual = "7 %"
else:
    reajuste = salario * percentual_5
    em_percentual = "4 %"

novo_salario = salario + reajuste

print (f"Novo salario: {novo_salario:.2f}")
print (f"Reajuste ganho: {reajuste:.2f}")
print (f"Em percentual: {em_percentual}")