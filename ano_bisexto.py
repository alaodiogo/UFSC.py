while True:
    ano = int(input("Digite o ano que gostaria de verificar: "))
    if ano == 0:
        break
    if ano % 4 == 0 and ano % 100 > 0 or ano % 400 == 0:
        print(f"{ano} é bissexto!")
    else:
        print(f"{ano} não é bissexto!")