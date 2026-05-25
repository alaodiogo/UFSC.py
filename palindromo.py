frase = input()

frase_limpa = ''

for caracteres in frase.lower():
    if caracteres.isalpha():
        frase_limpa += caracteres
        
print(frase_limpa == frase_limpa[::-1])