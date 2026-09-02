num1, num2 = [int(x) for x in input("Digite o intervalo de números que gostaria de somar: ").split()]

soma = sum(range(num1, num2 + 1)) #Soma necessaria pois sem ela o python termina no 99 e não no 100

print(f"A soma dos intervalos de {num1} e {num2} é {soma}")