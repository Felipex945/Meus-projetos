somaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0

for p in range(1,5):
    print(f"----- {p}ª PESSOAS ------")
    nome = (input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    somaidade += idade

    if sexo == "M" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
        
    if sexo == "F" and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4

print(f"A média de idade do grupo é {mediaidade} anos.")
if nomevelho:
    print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.")
else:
    print("Não há homens no grupo.")
print(f"Ao todo possuem {totmulher20} com menos de 20 anos.")
