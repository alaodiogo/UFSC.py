while True:
    resultado = 0
    n1, n2 = input("Digite os números que gostaria de cálcular: ").split()
    operacao = input("Digite a operação que gostaria de realizar (+, -, x, ÷): ")
    if operacao == "+":
        resultado = float(n1) + float(n2)
    elif operacao == "-":
        resultado = float(n1) - float(n2)
    elif operacao == "*" or operacao == "x":
        resultado = float(n1) * float(n2)
    else:
        resultado = float(n1) / float(n2)
    print(resultado)
    