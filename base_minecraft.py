nome_jogador = input("Qual e o seu nome? ")
qtd_madeira = int(input("Quantos blocos de madeira você tem? "))
qtd_pedra = int(input("Quantos blocos de pedra você tem? "))
qtd_contrucao_base = int(input("Quantos blocos você precisa para construir sua base? "))
sobra_madeira = 0
sobra_pedra = 0

madeira_suficiente = qtd_madeira >= 120
pedra_suficiente = qtd_pedra >= 250

if qtd_madeira > 120:
    sobra_madeira = qtd_madeira - 120
if qtd_pedra > 250:
    sobra_pedra = qtd_pedra - 250
    
if madeira_suficiente == False and pedra_suficiente == False:
    print(f"Você não possui a quantidade de pedras e madeiras necessárias para a contrução da base!")
elif pedra_suficiente == False:
    print(f"Você não possui a quantidade de pedras necessárias para a contrução da base!")
elif madeira_suficiente == False:
    print(f"Você não possui a quantidade de madeira necessárias para a contrução da base!")
else:
    print(f"Você possui a quantidade de materiais necessárias para a contrução da base!")


if sobra_madeira > 0 or sobra_pedra > 0:
    print(f"Foi usado 120 blocos de madeira e 250 blocos de pedra!")
    
print(f"Detalhes do estoque de {nome_jogador} pós construção:")
print(f"Total de pedras: {sobra_pedra}")
print(f"Total de madeiras: {sobra_madeira}")