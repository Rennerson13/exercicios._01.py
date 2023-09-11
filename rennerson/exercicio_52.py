import math
raiz=math.sqrt

lado=float(input("\nDigite o lado: "))

perimetro=lado*4
area=lado**2
diagonal=lado*raiz(2)

print(f"\nPerímetro: {perimetro}")
print(f"\nÁrea: {area}")
print(f"\nDiagonal: {diagonal}")
print("\n")