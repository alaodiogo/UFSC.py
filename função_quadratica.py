import math

bha_a = int(input(""))
bha_b = int(input(""))
bha_c = int(input(""))

#Calculo de mais e menos da fórmula Bhaskara
bha_mais = (-bha_b+math.sqrt((bha_b**2)-4*bha_a*bha_c))/(2*bha_a)
bha_menos = (-bha_b-math.sqrt((bha_b**2)-4*bha_a*bha_c))/(2*bha_a)

print (bha_mais, bha_menos)