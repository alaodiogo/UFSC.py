soma = 0
while True:
    num = int(input("Digite um número: "))
    if num == 21:
        break
    else:
        soma += num
        
print(f"A soma dos números é: {soma}")