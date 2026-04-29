tamanho_sequencia = int(input())
soma = 0

for _ in range(tamanho_sequencia):
    valor = float(input())
    soma += valor
    
media = soma / tamanho_sequencia

print (media)