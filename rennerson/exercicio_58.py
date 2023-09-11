import math

log=math.log

xnum1=float(input("\nEntre com o primeiro valor: "))
xnum2=float(input("\nEntre com o segundo valor: "))
xnum3=float(input("\nEntre com o terceiro valor: "))

x=xnum1+(xnum2/(xnum3+xnum1))+(2*(xnum1-xnum2))+log(64)/log(2)

print(f"\nX = {x}")
print("\n")