soma = 0

for i in range(5):
    num = int(input("Digite um número: "))
    if num < 0:
        continue
    else:
        soma += num
print(f"Total: {soma}")