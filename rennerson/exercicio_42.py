import math

pi=math.pi

angulo=int(input(f"Digite um ângulo: "))
range=(angulo*pi)/180

seno=math.sin(angulo)
cosseno=math.cos(angulo)
tangente=math.tan(angulo)
secante=1/math.sin(angulo)
cosecante=1/math.cos(angulo)
cotangente=1/math.tan(angulo)

print(f"\nSeno de {angulo} graus é: {seno}")
print(f"\nCosseno de {angulo} graus é: {cosseno}")
print(f"\nTangente de {angulo} graus é: {tangente}")
print(f"\nSecante de {angulo} graus é: {secante}")
print(f"\nCo-secante de {angulo} graus é: {cosecante}")
print(f"\nCo-tangente de {angulo} graus é: {cotangente}")
print("\n")
