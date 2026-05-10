tamanho_sequencia = int(input())
numeros = []
for i in range(tamanho_sequencia):
    numero = int(input())
    numeros.append(numero)

menor_numero = min(numeros)
print(menor_numero)