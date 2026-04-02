import math
n = float(input())
min_formula = 1.25506

minimo = n / math.log(n)
maximo = (n / math.log(n)) * min_formula

print (f"{minimo:.1f} {maximo:.1f}")