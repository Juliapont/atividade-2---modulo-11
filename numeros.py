# Criação da lista inicial com números de 1 a 50
numeros = list(range(1, 51))

# Mostrando cada número da lista inicial
print("Números de 1 a 50:")
for numero in numeros:
    print(numero)

# Adicionando novos números à lista (51 e 52 como exemplo)
numeros.append(51)
numeros.append(52)

# Mostrando a lista atualizada
print("\nNúmeros atualizados:")
for numero in numeros:
    print(numero)
