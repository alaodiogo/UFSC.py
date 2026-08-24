produto_a = float(input("Digite o valor do produto A: "))
produto_b = float(input("Digite o valor do produto B: "))

mais_caro = produto_a > produto_b
mesmo_preco = produto_a == produto_b

print(f"O produto A e mais caro que o produto B? {mais_caro}")
print(f"O produto A tem o mesmo valor do produto B? {mesmo_preco}")