usuario = input("Digite o Usuário: ")
senha = input("Digite a senha: ")

login_valido = usuario == 'admin' and senha == '1234'

print(f"Login autorizado? {login_valido}")