pedido = int(input("Escolha seu lanche conforme o cardápio: "))
total = 0

match pedido:
    case 1:
        total = 8.00
        lanche = "Cachorro-Quente"
    case 2:
        total = 12.00
        lanche = "X-Salada"
    case 3:
        total = 15.00
        lanche = "X-Bacon"
    case 4:
        total = 5.00
        lanche = "Refrigerante"
        
print(f"Você pediu {lanche} portanto seu total é R$ {total:.2f}")