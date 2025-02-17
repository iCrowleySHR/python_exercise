# Join: Junta os elementos de uma lista com um separador específico

# Exemplo 1
name = ["Ana", "Carlos", "Bruna"]
result = " ".join(name)  # Junta com espaços
print(result)  # Ana Carlos Bruna

# Exemplo 2
letras = ["P", "y", "t", "h", "o", "n"]
resultado = "".join(letras)  # Sem separador
print(resultado)  # Python

# Exemplo 3
linhas = ["Linha 1", "Linha 2", "Linha 3"]
resultado = "\n".join(linhas)  # Cada elemento em uma linha
print(resultado)
# Saída:
# Linha 1
# Linha 2
# Linha 3