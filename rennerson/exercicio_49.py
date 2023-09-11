n=int
nome=input("Entre com um nome: ")

primeiro_caracter=nome[0]
ultimo_caracter=nome[-1]
quarto_caracter=nome[3]
todos_menos_primeiro=nome[1:len(nome)]
dois_ultimos=nome[(len(nome)-2):len(nome)]

print(f"\nTodo nome: {nome}")
print(f"\nPrimeiro caractere: {primeiro_caracter}")
print(f"\nÚltimo caracter: {ultimo_caracter}")
print(f"\nTodos menos o primeiro caracter: {todos_menos_primeiro}")
print(f"\nDois últimos caracteres: {dois_ultimos}")
