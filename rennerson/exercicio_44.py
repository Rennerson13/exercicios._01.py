import math

log=math.log

num=float(input("\nEntre com o logaritmando: "))
base=float(input("\nEntre com a base: "))

logaritmo=log(num)/log(base)

print(f"Logaritmo de {num} na base {base}: {logaritmo}")
print("\n")
