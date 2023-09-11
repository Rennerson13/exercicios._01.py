deposito=float(input("\nEntre com o deposito: "))
taxa=float(input("\nEntre com a taxa de juros: "))

valor=int((deposito*taxa)/100)
total=int(deposito+valor)

print(f"\nRendimentos: {valor}\nTotal: {total}")
print("\n")