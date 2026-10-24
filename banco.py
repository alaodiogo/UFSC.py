class Conta_bancaria:
    def __init__(self, titular, saldo, num_conta, agencia, tipo_conta):
        self.titular = titular
        self.saldo = saldo
        self.num_conta = num_conta
        self.agencia = agencia
        self.tipo_conta = tipo_conta
        
    def depositar(self, deposito):
        self.saldo += deposito
        
    def sacar(self, saque):
        self.saldo -= saque
        
    def mostrar_saldo(self):
        print(f"Saldo atual: {self.saldo:.4f}")
        
    def info_conta(self):
        print(f"O número da sua conta é {self.num_conta}, sua agência é {self.agencia} e sua conta e",
              f"do tipo {self.tipo_conta}")
        
conta1 = Conta_bancaria("João Oliveira Santos", 23.255, "222599-8", 689, "Corrente")

while True:
    operacao = int(input(
f"""
Olá, {conta1.titular}! Selecione o que deseja fazer: 
1. Depósito
2. Saque
3. Saldo da conta
4. Informações da conta
5. Sair
"""
    ))

    match operacao:
        case 1:
            conta1.depositar(float(input("Quanto gostaria de depositar? ")))
            conta1.mostrar_saldo()
        case 2:
            conta1.sacar(float(input("Quanto gostaria de sacar? ")))
            conta1.mostrar_saldo()
        case 3:
            conta1.mostrar_saldo()
        case 4:
            conta1.info_conta()
        case 5:
            break
        case _:
            print("Operação inválida")



