lista_numeros = []

while True:
    numeros = int(input())
    if numeros == 0:
        break
    lista_numeros.append(numeros)

quantidade_numeros = len(set(lista_numeros))

print (quantidade_numeros)