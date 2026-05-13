inicio = 1 # Para suprir a condição de inicio do while
alcool = 0
gasolina = 0
diesel = 0

while inicio > 0:
    tipo_combustivel = int(input())
    match tipo_combustivel:
        case 1:
            alcool += 1
        case 2:
            gasolina += 1
        case 3:
            diesel += 1
        case 4:
            break
    
print ("MUITO OBRIGADO")
print (f"Alcool: {alcool}")
print (f"Gasolina: {gasolina}")
print (f"Diesel: {diesel}")
