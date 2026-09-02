palavra = input("Digite uma palavra: ").lower()
vogais = 0

for letra in palavra:
    match letra:
        case "a":
            vogais += 1
        case "e":
            vogais += 1
        case "i":
            vogais += 1
        case "o":
            vogais += 1
        case "u":
            vogais += 1
        case _:
            continue
print(f'A palavra "{palavra}" contém {vogais} vogais')