soma = 0
cont = 0

for c in range(1, 7):
    num = int(input(f"Digite o {c} número: "))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f"Você informou {cont} números PARES e a soma foi {soma}")