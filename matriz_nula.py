matriz = [
    ["Garuda", "", "Arch"],
    ["", "Linux", ""],
    ["Thonny", "Python", "UFSC"]
]

def contar_nulos(matriz):
    resultado = 0
    for linha in matriz:
        for coluna in linha:
            if coluna == "":
                resultado += 1
    return resultado
                
print(contar_nulos(matriz))
