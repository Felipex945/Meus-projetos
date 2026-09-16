nome = str(input('Digite seu nome: ')).strip()
p_nome = nome.split()

print(f"Muito prazer em te conhecer {nome}")
print(f"Seu primeiro nome é {p_nome[0]}")

# O índice -1 sempre aponta para o último item da lista
print(f"O seu último nome é {p_nome[-1]}")