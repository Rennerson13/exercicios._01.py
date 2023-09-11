import math as m

pr1=float(input("\nDigite a PR1: "))
pr2=float(input("\nDigite a PR2: "))

mf=(pr1+pr2)/2

print(f"\nMédia truncada: {round((mf-0.5)+0.001)}")
print(f"\nMédia arredondada: {round(mf+0.001)}")
print("\n")
