import math

base=float(input("Digite a base: "))
altura=float(input("Digite a altura: "))

perimetro=float(2*(base+altura))
area=float(base*altura)
diagonal=float(math.sqrt(base**2+altura**2))

print(f"\nPerimetro: {perimetro}")
print(f"\nÁrea: {area}")
print(f"\nDiagonal: {diagonal}")
print("\n")
