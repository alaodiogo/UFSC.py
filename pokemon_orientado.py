import random

class Pokemon:
    def __init__(self, nome, tipo, vida, forca):
        self.nome = nome
        self.tipo = tipo
        self.vida = vida
        self.forca = forca
        
    def atacar(self, alvo):
        dano = (self.forca * random.randint(1, 10))
        alvo.vida = max(0, alvo.vida - dano)
        
    def esta_vivo(self):
        return self.vida > 0
        
pokemon1 = Pokemon("Pikachu", "Elétrico", 1000, 55)
pokemon2 = Pokemon("Bulbasauro", "Grama", 1000, 49)

while pokemon1.esta_vivo() and pokemon2.esta_vivo():
    pokemon1.atacar(pokemon2)
    if pokemon2.esta_vivo():
        pokemon2.atacar(pokemon1)
        
if pokemon1.esta_vivo():
    print("Pikachu ganhou de Bulbasauro!")
else:
    print("Bulbasauro ganhou de Pikachu!")