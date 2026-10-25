matriz = [
    [2, 4, 5, 8],
    [9, 11, 1, 13]
]


def e_primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


resultado = True
contador_primos = 0

for linha in matriz:
    for elemento in linha:
        resultado = e_primo(elemento)
        if resultado == True:
            contador_primos += 1
            
print(contador_primos)
