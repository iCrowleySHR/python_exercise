# Cria uma lista com quatro strings
valor = ["karla", "gonçalves", "dos", "santos"]

# Percorre a lista usando enumerate, que fornece o índice e o valor ao mesmo tempo
for indice, data in enumerate(valor):
    # Imprime o índice e o valor correspondente
    print(f"{indice} : {data}")

# Percorre a lista diretamente, acessando apenas os valores
for name in valor:
    # Imprime apenas o valor (nome), sem o índice
    print(name)

# Percorre a lista usando índices, com range e len
for i in range(len(valor)):
    # Acessa o valor na posição 'i' da lista e imprime junto com o índice
    print(f"{i} : {valor[i]}")

# Junta todos os elementos da lista em uma única string, separados por espaço
resultado = " ".join(valor)

# Imprime a string final com todos os nomes juntos
print(resultado)

