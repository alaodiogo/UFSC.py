jogador = input("Qual é o seu nome? ")
total_dinheiro = float(input("Quanto de dinheiro você tem? "))
print("Informe abaixo o valor dos seguinte itens: Colete, granada de fumaça e kit de desarme")
valor_colete = float(input())
valor_granada = float(input())
valor_kit = float(input())

total_compra = valor_colete + valor_granada + valor_kit
sobra_compra = total_dinheiro - total_compra
compra_efetuada = sobra_compra >= 0

print(f"======================")
print(f"      {jogador}       ")
print(f"======================")

print(f"Dinheiro total: {total_dinheiro}")
print(f"Total da compra: {total_compra}")
if sobra_compra >= 0:
    print(f"Compra autorizada? {compra_efetuada}")
    print(f"Dinheiro restante: {sobra_compra:.2f}")
else:
    print(f"Compra autorizada? {compra_efetuada}")
    print("Você não possui o saldo necessario para a compra!")
