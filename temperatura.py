temp = int(input("Digite a temperatura em graus Celsius: "))

temp_alta = temp > 30
temp_baixa = temp <= 0

print(f"A temperatura está a mais de 30º Celsius? {temp_alta}")
print(f"A temperatura está a menos de 0º Celsius? {temp_baixa}")