valor=float(input("\nDigite o valor da prestação: "))
taxa=float(input("\nDigite o valor da taxa: "))
tempo=int(input("\nDigite o tempo(Número de meses): "))

prest=valor+(valor*(taxa/100)*tempo)

print(f"\nO valor da prestação é: {prest}")
print("\n")
