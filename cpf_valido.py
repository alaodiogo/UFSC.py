cpf = input()
peso = 2
multiplicacao = 0

# Para verificar se o cpf contem ponto e digito
if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
    cpf = cpf.replace('.', '').replace('-', '')

# Para verificar o primeiro digito
for caractere in reversed(cpf[0:-2]):
    multiplicacao += int(caractere) * peso
    peso += 1

mod_primeiro_digito = 11 - (multiplicacao % 11)
peso = 2  # Para reiniciar o valor base do peso
multiplicacao = 0  # Para limpar a multiplicação anterior

# Para verificar o segundo digito
for caractere in reversed(cpf[0:-1]):
    multiplicacao += int(caractere) * peso
    peso += 1

mod_segundo_digito = 11 - (multiplicacao % 11)

# Verifica se a regra seguinte está sendo seguida: "Caso a subtração de cada digito verificador der mais de 9, o digito verififcador será automaticamente 0"
if mod_primeiro_digito > 9:
    mod_primeiro_digito = 0
if mod_segundo_digito > 9:
    mod_segundo_digito = 0

resultado = str(mod_primeiro_digito) == cpf[-2] and str(mod_segundo_digito) == cpf[-1]

if cpf == cpf[0] * 11:
    resultado = False

print(resultado)