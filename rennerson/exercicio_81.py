conta=input("\nDigite uma conta de três dígitos: ")

inv = int(conta[::-1])
conta = int(conta)

d1=int(conta/100)
d2=int(conta%100/10)
d3=int(conta%100%10)

soma=conta+inv

d1=int(soma/100*1)
d2=int(soma%100/10)*2
d3=int(soma%100%10)*3

digito=(d1+d2+d3)%10

print(f"\nDígito verificador: {digito}")
print("\n")