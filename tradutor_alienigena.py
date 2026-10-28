class TradutorAlienigena:
    
    def __init__(self):
        self.idiomas = ["Humano", "Marciano", "Jupiteriano"]
        
    def escolha_idioma(self):
        while True:
            idioma_escolhido = 0
            try:
                idioma_escolhido = int(input(
"""
Escolha o idioma abaixo:
1. Humano
2. Marciano
3. Jupiteriano
"""))
                return self.idiomas[idioma_escolhido]
                break
            except:
                print("Digite um número valido!")
        
    def traduzir_numero(self):
        while True:
            try:
                num = int(input("Digite um número inteiro: "))
                return 100 / num
            except ValueError:
                print("Digite um número inteiro")
        
    def iniciar(self):
        self.escolha_idioma()
        self.traduzir_numero()

objeto = TradutorAlienigena()

objeto.iniciar()
