lista_nomes_1 = []
lista_nomes_2 = []

while True:
    tamanho_lista_1 = int(input())
    for i in range(tamanho_lista_1):
        lista_nomes_1.append(input())
    tamanho_lista_2 = int(input())
    for l in range(tamanho_lista_2):
        lista_nomes_2.append(input())
    break
    
lista_final = lista_nomes_1 + lista_nomes_2
lista_final.sort()
for nomes in lista_final:
    print(nomes)