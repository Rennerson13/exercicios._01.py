tempo=float(input("\nDigite o tempo gasto: "))
vel=float(input("\nDigite a velocidade média: "))

dist=float(tempo*vel)
litros=float(dist/12)

print(f"\nVelocidade: {vel}, tempo: {tempo}, distância: {dist}, litros: {litros:.2f}")
print("\n")