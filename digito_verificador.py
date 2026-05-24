numero = input()
peso = 2
multiplicacao = 0

for caractere in reversed(numero[0:-1]):
    multiplicacao += int(caractere) * peso
    peso += 1

mod = 11 - (multiplicacao % 11)

if mod > 9:
    mod = 0

resultado = str(mod) == numero[-1]

print(resultado)