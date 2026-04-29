comprimento_mesa = float(input())
largura_mesa = float(input())
numero_gavetas = float(input())
tipo_madeira = input()

preco_minimo_de_pedido = 200.0
custo_metro_quadrado = 100
adicional_gavetas = 30
total_madeira = 0
total_largura = 0
total_gavetas = 0

total_metro = (comprimento_mesa * largura_mesa) * custo_metro_quadrado

if largura_mesa > 2:
    total_largura = 50
    
match tipo_madeira:
    case 'mogno':
        total_madeira = 150
    case 'carvalho':
        total_madeira = 125
        
total_gavetas = numero_gavetas * adicional_gavetas
    
valor_total = total_metro + total_gavetas + total_madeira + total_largura

total_a_pagar = max(valor_total, preco_minimo_de_pedido)

print (total_a_pagar)