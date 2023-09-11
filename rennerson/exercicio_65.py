import math

pi=math.pi

altura=int(input("\nDigite a altura da lata: "))
raio=int(input("\nDigite o raio da lata: "))

volume=pi*(raio**2)*altura

print(f"\nO volume da lata é: {volume:.2f}")
print("\n")
