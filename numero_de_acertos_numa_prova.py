gabarito = input()
respostas_maria = input()

acertos = 0

for respostas in range(len(gabarito)):
    if gabarito[respostas] == respostas_maria[respostas]:
        acertos += 1

print(acertos)