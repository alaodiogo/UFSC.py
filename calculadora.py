def calculadora(operacao, n1, n2):
    match operacao:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*" | "x":
            return n1 * n2
        case "/":
            if n2 == 0:
                return 0
            else:
                return n1 / n2
        case "^":
            return n1 ** n2
        case "%":
            return n1 % n2

while True:
    operacao = input("Qual operação gostaria de realizar? (+, -, x, ÷, ^, %) ")
    n1, n2 = [int(x) for x in input("Digite os números que gostaria de calcular: ").split()]
    total = calculadora(operacao, n1, n2)
    print(f"O resultado da operação é: {total}")