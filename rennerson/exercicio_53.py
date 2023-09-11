import math
raiz=math.sqrt

base=float(input("\nEntre com a base: "))
altura=float(input("\nEntre com a altura: "))
profundidade=float(input("\nEntre com a profundidade: "))

diagonal=raiz(base**2+altura**2+profundidade**2)

print(f"\nDiagonal: {diagonal}")
print("\n")
