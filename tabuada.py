num = int(input("Digite um número que gostaria de ver a tabuada: "))
multi = 0

for i in range(1, 11):
    multi = num * i
    print(f"{num} x {i} = {multi}")