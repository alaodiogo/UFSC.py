nota = input("Qual foi se conceito de nota? ")

match nota:
    case "A":
        print("Excelente! Aprovado com louvor")
    case "B":
        print("Muito bom! Aprovado")
    case "C":
        print("Regular, aprovado por média")
    case "D":
        print("Insuficiente, recuperação!")
    case "E":
        print("Reprovado!")
    case _:
        print("Nota invalida!")