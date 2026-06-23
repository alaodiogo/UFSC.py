num_casos = int(input())

for i in range(num_casos):
    idade_jogadores = [int(x) for x in input().split()]
    idade_jogadores.pop(0)
    idade_capitao = idade_jogadores[len(idade_jogadores) // 2]
    print (f"Case {i+1}: {idade_capitao}")