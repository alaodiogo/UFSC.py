horario = input("Você pretende embarcar no horário de pico? ")
idade = int(input("Qual sua idade? "))
tipo_cartao = input("Qual o tipo do seu cartão? ")
tarifa = 0

if idade >= 65 and tipo_cartao == 'idoso' and horario == 'sim': #Idoso
    tarifa = 0
else:
    tarifa = 2.50
if tipo_cartao == 'estudante' and horario == 'sim': #Estudante
    tarifa = 4.50
else:
    tarifa = 2.50
if tipo_cartao == 'comum' and horario == 'sim':
    tarifa = 6.00
else:
    tarifa = 4.00
    
if horario == 'sim':
    print(f"Você possui o cartão do tipo {tipo_cartao} então no horário de pico pagará R${tarifa:.2f}")
else:
    print(f"Você possui o cartão do tipo {tipo_cartao} então fora do horário de pico pagará {tarifa:.2f}")
