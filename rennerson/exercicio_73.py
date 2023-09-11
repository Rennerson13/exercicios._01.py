num = float(input("Entre com um numero com parte fracionária: "))
numi = round((num - 0.5))
numfrac = num - numi
numa = round(num + 0.00001)

print(f"\nA parte inteiro: {numi}")
print(f"\nA parte fracionada: {numfrac+0.00001:.4f}")
print(f"\nNúmero arredondado: {numa}")
print("\n")