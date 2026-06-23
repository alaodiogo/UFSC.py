while True:
    qtd_casos = int(input())
    
    if qtd_casos == 0:
        break
    
    for i in range(qtd_casos):
        alternativas = [int(x) for x in input().split()]
        qtd_marcacoes = 0
        
        for resposta in alternativas:
            if resposta <= 127:
                qtd_marcacoes += 1
                escolha_aluno = alternativas.index(resposta)
                
        if qtd_marcacoes == 1:
            match escolha_aluno:
                case 0:
                    resposta_aluno = 'A'
                case 1:
                    resposta_aluno = 'B'
                case 2:
                    resposta_aluno = 'C'
                case 3:
                    resposta_aluno = 'D'
                case 4:
                    resposta_aluno = 'E'
        else:
            resposta_aluno = "*"
                                    
        print (resposta_aluno)