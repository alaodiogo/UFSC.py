qtd_casos = int(input())

for casos in range(qtd_casos):
    tem_parentese = 0
    formulas = input()
    for i in formulas:
        if i == "(":
            tem_parentese += 1
        elif i == ")":
            tem_parentese -= 1
        if tem_parentese < 0:
            break
            
    if tem_parentese == 0:
        print("correct")
    else:
        print("incorrect")