numero = int(input())
dobro = 0 #Variavél usada para guardar a dobra do primeiro expoente
exponenciacao = 0

while numero > 0:
    dobro += 2
    exponenciacao = dobro ** 2
    if dobro > numero:
        break
    print(f"{dobro}^2 = {exponenciacao}")
    