matrizz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def soma_matriz(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    somas = []
    for c in range(num_colunas):
        soma_atual = 0
        for l in range(num_linhas):
            soma_atual += matriz[l][c]
        somas.append(soma_atual)
    return somas
            
print(soma_matriz(matrizz))