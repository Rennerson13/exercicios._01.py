sm=float(input("\nEntre com o salário mínimo: "))
qntdade=float(input("\nEntre com a quantidade em quilowatt: "))

preco=sm/700

vp=preco*qntdade
vd=vp*0.9

print(f"\nPreço do Quilowatt: {preco}, valor a ser pago: {vp}")
print(f"\nPreço com desconto: {vd}")
print("\n")
