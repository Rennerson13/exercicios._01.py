p=float(input("\nDigite o valor da aplicação: "))
i=float(input("\nDigite a taxa ( 0 - 1 ): "))
n=int(input("Digite o número de meses: "))

va=p*(((1+i)**n)-1)/i

print(f"\nO valor acumulado é: {va}")
print("\n")