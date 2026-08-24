idade = int(input("Digite sua idade: "))

crianca = idade < 12
adolescente = 12 <= idade <= 17
adulto = 18 <= idade <= 64
idoso = idade >= 65

print(f"É criança? {crianca}")
print(f"É adolescente? {adolescente}")
print(f"É adulto? {adulto}")
print(f"É idoso? {idoso}")