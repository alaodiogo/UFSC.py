senha_correta = 1234
tentativas = 0
while True:
    senha = int(input("Digite sua senha: "))
    if senha < 0:
        continue
    elif senha == 0:
        print("0 é um número proibido!")
        break
    elif senha != 1234:
        print("Acesso negado!")
        tentativas += 1
    else:
        print(f"Acesso liberado! Você tentou {tentativas} vezes seu login!")
        break